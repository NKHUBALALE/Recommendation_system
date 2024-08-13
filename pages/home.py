import streamlit as st

def display():
    """Home page content"""
    st.title("Anime Recommendation System")
    st.subheader("Explore and discover new anime")
    st.markdown("""
        This application helps you discover new anime based on your preferences. Explore various anime and get personalized recommendations.
        Use the sidebar to navigate to different sections of the application, including Information, EDA (Exploratory Data Analysis), Recommendation, Feedback, and About Us.
    """)
