import streamlit as st

def display():
    """About Us Page"""
    st.info("About Us")

    st.markdown(
        """
        This application was developed by Team JB3, a group of data science enthusiasts from the ExploreAI academy, as part of an unsupervised learning project. Our goal is to provide personalized anime recommendations based on user preferences and behaviors. By leveraging advanced recommendation algorithms and exploratory data analysis, we aim to enhance your anime discovery experience.

        This system uses collaborative filtering and content-based techniques to suggest anime that you might enjoy, helping you find new favorites based on your interests.

        We are always open to new project collaborations and would love to explore innovative ideas and partnerships. The world is in safe hands with us. For more information or inquiries, please contact us at JB3unsupervised@sandtech.co.za.

        Thank you for your interest and support!
        """
    )
