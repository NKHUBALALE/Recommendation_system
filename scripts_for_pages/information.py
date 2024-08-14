import streamlit as st

def display():
    """Information page content"""
    st.title("Information")

    st.info("General Information")

    st.markdown(
        """
        The purpose of this recommendation system is to provide personalized anime suggestions based on user preferences.
        
        ### How to Use the App:

        1. **Choose a Recommendation Method:**
           - You can choose between "Collaborative Filtering" and "Content-Based Filtering" methods.
           - **Collaborative Filtering:** Enter your User ID to get anime recommendations based on what similar users have enjoyed.
           - **Content-Based Filtering:** Enter up to 3 anime titles that you like, and the system will recommend similar anime based on their features.
        
        2. **Input Your Preferences:**
           - For **Collaborative Filtering**, simply enter your User ID and click "Get Recommendations."
           - For **Content-Based Filtering**, enter the titles of up to 3 anime you like (comma-separated) and click "Get Recommendations."

        3. **View Your Recommendations:**
           - The app will display a list of recommended anime titles along with images and predicted ratings or similarity scores.

        ### Methodology:

        This application utilizes various recommendation techniques including collaborative filtering and content-based filtering to suggest anime that you might enjoy.

        ### Documentation:

        - **Collaborative Filtering:** This method makes automatic predictions about the interests of a user by collecting preferences from many users (collaborating).
        - **Content-Based Filtering:** This method uses item features (e.g., genres, directors) to recommend other items similar to what the user likes.

        ### Notes:
        - Ensure that the User ID you enter is a valid integer within the dataset for Collaborative Filtering.
        - When entering anime titles for Content-Based Filtering, make sure they match the format used in the dataset. For example:
            - Use "Dragon Ball Z" instead of "DRAGON BALL Z" or "Dragon ball", the first letter of each word must be a capital letter!
            - For titles with multiple names, like "One Piece: Strong World," ensure you include all parts of the title exactly as they appear in the dataset.
        - The recommendation system requires an active internet connection to fetch anime images from external sources.
        """
    )

