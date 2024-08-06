import pandas as pd
import pickle
import streamlit as st
import os
import requests

# Custom CSS for anime style
anime_style = """
<style>
body {
    background-color: #f0f0f0;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    color: #333;
}
h1 {
    color: #ff6699;
    text-shadow: 2px 2px #ffb3d9;
}
h2, h3, h4 {
    color: #ff6699;
}
.sidebar-section {
    background-color: #28a745;
    padding: 10px;
    border-radius: 10px;
}
.sidebar-section p {
    color: white;
}
.stButton>button {
    background-color: #ff6699;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px;
    font-size: 16px;
    cursor: pointer;
}
.stButton>button:hover {
    background-color: #ff4da6;
}
.stTextInput>div>div>input {
    border: 2px solid #ff6699;
    border-radius: 5px;
    padding: 5px;
}
.stTextArea>div>div>textarea {
    border: 2px solid #ff6699;
    border-radius: 5px;
    padding: 5px;
}
.anime-title {
    font-size: 20px; /* Adjust font size as needed */
    color: #ff6699; /* Same color as the heading */
    font-weight: bold;
}
</style>
"""

# Define file paths
model_chunk_files = ['SVD model files/model_part_0.pkl', 'SVD model files/model_part_1.pkl', 'SVD model files/model_part_2.pkl']
anime_data_path = 'anime_cleaned.csv'
train_data_path = 'train_cleaned.csv'

def load_svd_model(chunk_files):
    data = b''
    for chunk_file in chunk_files:
        if os.path.isfile(chunk_file):
            with open(chunk_file, 'rb') as f:
                data += f.read()
        else:
            st.error(f"File not found: {chunk_file}")
            return None
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
        # Ensure user_id is an integer
        user_id = int(user_id)

        # Get the list of all anime IDs
        all_anime_ids = anime_data['anime_id'].unique()

        # Get the list of anime IDs that the user has already rated
        rated_anime_ids = merged_df[merged_df['user_id'] == user_id]['anime_id']

        # Create test set with all anime that the user has not rated
        testset = [(user_id, anime_id, 0) for anime_id in all_anime_ids if anime_id not in rated_anime_ids]

        # Make predictions
        predictions = model.test(testset)

        # Convert predictions to a DataFrame with formatted ratings
        pred_df = pd.DataFrame([{
            'anime_id': pred.iid, 
            'predicted_rating': f"{round(pred.est, 1):.1f}"  # Format to one decimal place
        } for pred in predictions])

        # Merge with anime details
        recommendations = pd.merge(pred_df, anime_data, on='anime_id')
        recommendations = recommendations.sort_values(by='predicted_rating', ascending=False)

        # Return top 10 recommendations
        return recommendations.head(10)
    
    except Exception as e:
        st.write("An error occurred:", e)
        return pd.DataFrame()

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

def main():
    """Recommendation System App with Streamlit"""

    # Apply custom anime style
    st.markdown(anime_style, unsafe_allow_html=True)

    # Creates a main title and subheader on your page - these are static across all pages
    st.title("Anime Recommendation System")
    st.subheader("Explore and discover new anime")

    # Sidebar navigation tip in green
    st.sidebar.markdown(
        """
        <div class="sidebar-section">
            <p><b>Navigation Tip:</b></p>
            <p>Click the dropdown menu above to navigate between pages.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Sidebar with selection box for different pages
    options = ["Home", "Information", "EDA", "Recommendation", "Feedback", "About Us"]
    selection = st.sidebar.selectbox("Choose Option", options)

    # Building out the "Home" page
    if selection == "Home":
        st.info("Welcome to the Anime Recommendation System!")
        
        st.markdown(
            """
            This application helps you discover new anime based on your preferences. Explore various anime and get personalized recommendations.
            """
        )
        
        st.markdown(
            """
            Use the sidebar to navigate to different sections of the application, including Information, EDA (Exploratory Data Analysis), Recommendation, Feedback, and About Us.
            """
        )

    # Building out the "Information" page
    if selection == "Information":
        st.info("General Information")

        st.markdown(
            """
            The purpose of this recommendation system is to provide personalized anime suggestions based on user preferences.

            ### Methodology:

            This application utilizes various recommendation techniques including collaborative filtering and content-based filtering to suggest anime that you might enjoy.
            """
        )
        
        # Adding Documentation section
        st.markdown(
            """
            ### Documentation:

            - **Collaborative Filtering:** This method makes automatic predictions about the interests of a user by collecting preferences from many users (collaborating).
            - **Content-Based Filtering:** This method uses item features (e.g., genres, directors) to recommend other items similar to what the user likes.
            """
        )

    # Building out the "EDA" page
    if selection == "EDA":
        st.info("Exploratory Data Analysis")

        st.markdown(
            """
            Overview and Introduction:

            - The purpose of the Exploratory Data Analysis (EDA) is to examine the distribution of anime data, such as genres, ratings, and popularity.
            - Understanding the data helps in identifying patterns and potential biases, which are critical for developing accurate recommendation models.
            """
        )

        # Removed the image from the EDA section

    # Building out the Recommendation page
    if selection == "Recommendation":
        st.info("Anime Recommendations")

        user_id = st.text_input("Enter User ID", '')

        if user_id:
            recommendations = get_recommendations(user_id, best_svd_model, anime_data, merged_df)
            if not recommendations.empty:
                st.write("Based on the information we have, we think these are the anime you would love and how you'd rate them:")

                # Display the DataFrame without index and rounded ratings
                recommendations = recommendations[['anime_id', 'predicted_rating']]
                
                for index, row in recommendations.iterrows():
                    anime_id = row['anime_id']
                    
                    # Fetch the anime image and title from the API
                    title, image_url = fetch_anime_image(anime_id)
                    
                    if not title or not image_url:
                        # Use the title from the local dataset if API fails
                        title = anime_data.loc[anime_data['anime_id'] == anime_id, 'name'].values[0]
                        image_url = None
                    
                    # Display the anime information
                    if image_url:
                        st.markdown(
                            f"<div class='anime-title'>{title}</div> - You are likely to rate: {row['predicted_rating']}<br><img src='{image_url}' width='300'/>",
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f"<div class='anime-title'>{title}</div> - You are likely to rate: {row['predicted_rating']}",
                            unsafe_allow_html=True
                        )
            else:
                st.write("No recommendations available. Please check the user ID or try again later.")

    # Building out the Feedback page
    if selection == "Feedback":
        st.info("Feedback")

        st.markdown(
            """
            We value your feedback! Please provide your comments and suggestions to help us improve this application.
            """
        )

        feedback_text = st.text_area("Your Feedback", "")
        if st.button("Submit Feedback"):
            st.success("Thank you for your feedback!")

    # Building out the About Us page
    if selection == "About Us":
        st.info("About Us")

        st.markdown(
            """
            This application was developed by Team_MM1, a group of data science students from the ExploreAI academy under the supervised classification sprint [Team_MM1] as a project to classify news articles into categories using machine learning models. It demonstrates the use of various classification algorithms to analyze and categorize text data.

            For more information or inquiries, please contact us at mm1_classification@sandtech.co.za.
            """
        )

if __name__ == "__main__":
    main()
