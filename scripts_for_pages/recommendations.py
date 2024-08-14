import pandas as pd
import pickle
import os
import requests
import numpy as np
import streamlit as st

# Define file paths for recommendations
model_chunk_files = ['SVD model files/model_part_0.pkl', 'SVD model files/model_part_1.pkl', 'SVD model files/model_part_2.pkl']
anime_data_path = 'csv files/anime_cleaned.csv'
train_data_path = 'csv files/train_cleaned.csv'
tfidf_matrix_path = 'tfidf_matrix.pkl'
feature_names_path = 'feature_names.pkl'

# Function to load the SVD model
def load_svd_model(chunk_files):
    data = b''
    for chunk_file in chunk_files:
        if os.path.isfile(chunk_file):
            with open(chunk_file, 'rb') as f:
                data += f.read()
        else:
            raise FileNotFoundError(f"File not found: {chunk_file}")
    return pickle.loads(data)

# Load the SVD model
best_svd_model = load_svd_model(model_chunk_files)

# Load the anime data
anime_data = pd.read_csv(anime_data_path)

# Load the train data
train_cleaned = pd.read_csv(train_data_path)

# Load the TF-IDF matrix and feature names
with open(tfidf_matrix_path, 'rb') as f:
    tfidf_matrix = pickle.load(f)

with open(feature_names_path, 'rb') as f:
    feature_names = pickle.load(f)

# Merge the dataframes
merged_df = pd.merge(train_cleaned, anime_data, on='anime_id')

def get_recommendations(user_id, model, anime_data, merged_df):
    """Get recommendations using collaborative filtering."""
    try:
        user_id = int(user_id)
        all_anime_ids = anime_data['anime_id'].unique()
        rated_anime_ids = merged_df[merged_df['user_id'] == user_id]['anime_id']
        testset = [(user_id, anime_id, 0) for anime_id in all_anime_ids if anime_id not in rated_anime_ids]
        predictions = model.test(testset)
        pred_df = pd.DataFrame([{'anime_id': pred.iid, 'predicted_rating': f"{round(pred.est, 1):.1f}"} for pred in predictions])
        recommendations = pd.merge(pred_df, anime_data, on='anime_id')
        recommendations = recommendations.sort_values(by='predicted_rating', ascending=False)
        return recommendations.head(10)
    except Exception as e:
        raise RuntimeError(f"An error occurred while getting recommendations: {e}")

def fetch_anime_image(anime_id):
    """Fetch anime image using Jikan API."""
    url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    response = requests.get(url)
    if response.status_code == 200:
        anime_data = response.json()
        title = anime_data['data']['title']
        image_url = anime_data['data']['images']['jpg']['image_url']
        return title, image_url
    else:
        return None, None

def get_content_based_recommendations(user_animes, anime_data, tfidf_matrix, feature_names):
    """Get content-based recommendations based on precomputed TF-IDF matrix."""
    try:
        if not isinstance(user_animes, list):
            raise ValueError("user_animes should be a list of anime titles.")
        
        if len(user_animes) == 0:
            raise ValueError("No anime titles provided.")
        
        # Convert user_animes to DataFrame
        user_animes_df = anime_data[anime_data['name'].isin(user_animes)]
        
        if user_animes_df.empty:
            raise ValueError("None of the provided anime titles are in the dataset.")
        
        # Use 'genre' instead of 'description' for content-based filtering
        user_anime_genres = user_animes_df['genre'].tolist()
        user_anime_features = ' '.join(user_anime_genres)
        
        # Create the TF-IDF vector for user profile
        user_profile = np.zeros(len(feature_names))
        for word in user_anime_features.split():
            if word in feature_names:
                idx = feature_names.index(word)
                user_profile[idx] = 1  # Simplified; adjust weighting if needed
        
        if user_profile.shape[0] != tfidf_matrix.shape[1]:
            raise ValueError("Dimension mismatch between user profile and TF-IDF matrix.")
        
        # Normalize user profile vector
        norm = np.linalg.norm(user_profile)
        if norm != 0:
            user_profile = user_profile / norm
        
        # Compute scores for all anime
        scores = []
        for idx in range(tfidf_matrix.shape[0]):
            anime_vector = tfidf_matrix[idx].toarray()[0]
            norm_anime_vector = np.linalg.norm(anime_vector)
            if norm_anime_vector != 0:
                anime_vector = anime_vector / norm_anime_vector
            score = np.dot(user_profile, anime_vector)
            scores.append((anime_data.iloc[idx]['anime_id'], score))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        top_scores = scores[:10]
        
        recommended_animes = pd.DataFrame(top_scores, columns=['anime_id', 'score'])
        recommendations = pd.merge(recommended_animes, anime_data, on='anime_id')
        recommendations = recommendations.sort_values(by='score', ascending=False)
        return recommendations.head(10)
    
    except Exception as e:
        raise RuntimeError(f"An error occurred while getting content-based recommendations: {e}")

# Streamlit UI
st.title("Anime Recommendations")

# Choose recommendation method
recommendation_method = st.selectbox(
    "Choose Recommendation Method",
    ["Collaborative Filtering", "Content-Based Filtering"]
)

if recommendation_method == "Collaborative Filtering":
    user_id = st.text_input("Enter User ID")
    if st.button("Get Recommendations"):
        try:
            recommendations = get_recommendations(user_id, best_svd_model, anime_data, merged_df)
            st.write("Recommendations:")
            for _, row in recommendations.iterrows():
                title, image_url = fetch_anime_image(row['anime_id'])
                if image_url:
                    st.image(image_url, caption=title)
                st.write(f"{row['name']}: {row['predicted_rating']}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

elif recommendation_method == "Content-Based Filtering":
    user_animes = st.text_input("Enter up to 3 Anime Titles (comma separated)").split(',')
    user_animes = [anime.strip() for anime in user_animes if anime.strip()]
    if st.button("Get Recommendations"):
        try:
            recommendations = get_content_based_recommendations(user_animes, anime_data, tfidf_matrix, feature_names)
            st.write("Recommendations:")
            for _, row in recommendations.iterrows():
                title, image_url = fetch_anime_image(row['anime_id'])
                if image_url:
                    st.image(image_url, caption=title)
                st.write(f"{row['name']}: {row['rating']}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
