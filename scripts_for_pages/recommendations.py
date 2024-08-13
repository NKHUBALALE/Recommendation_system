# recommendations.py

import pandas as pd
import pickle
import os
import requests

# Define file paths for recommendations
model_chunk_files = ['SVD model files/model_part_0.pkl', 'SVD model files/model_part_1.pkl', 'SVD model files/model_part_2.pkl']
anime_data_path = 'csv files/anime_cleaned.csv'
train_data_path = 'csv files/train_cleaned.csv'

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

# Merge the dataframes
merged_df = pd.merge(train_cleaned, anime_data, on='anime_id')

def get_recommendations(user_id, model, anime_data, merged_df):
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
        raise RuntimeError("An error occurred while getting recommendations:", e)

def fetch_anime_image(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    response = requests.get(url)
    if response.status_code == 200:
        anime_data = response.json()
        title = anime_data['data']['title']
        image_url = anime_data['data']['images']['jpg']['image_url']
        return title, image_url
    else:
        return None, None
