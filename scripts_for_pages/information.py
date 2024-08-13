import streamlit as st

def display():
    """Information page content"""
    st.title("Information")

    st.info("General Information")

    st.markdown(
        """
        The purpose of this recommendation system is to provide personalized anime suggestions based on user preferences.

        ### Methodology:

        This application utilizes various recommendation techniques including collaborative filtering and content-based filtering to suggest anime that you might enjoy.
        """
    )
    
    st.markdown(
        """
        ### Documentation:

        - **Collaborative Filtering:** This method makes automatic predictions about the interests of a user by collecting preferences from many users (collaborating).
        - **Content-Based Filtering:** This method uses item features (e.g., genres, directors) to recommend other items similar to what the user likes.
        """
    )
