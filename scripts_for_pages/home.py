import streamlit as st

def display():
    """Home page content"""
    st.title("Anime Recommendation System")

    st.info("Welcome to the Anime Recommendation System!")
    
    st.markdown(
        """
        This application helps you discover new anime based on your preferences. Whether you're a seasoned anime fan or new to the genre, our system offers personalized recommendations tailored to your tastes.

        ### Key Features:

        - **Personalized Recommendations:** Receive tailored anime suggestions using collaborative filtering or content-based filtering methods.
        - **Explore Anime:** Discover various anime titles and see how they are rated and categorized.
        - **Interactive Visualizations:** Check out the Exploratory Data Analysis (EDA) section to explore insights about anime distribution and other relevant statistics.
        - **Provide Feedback:** Share your thoughts or suggestions to help us improve the recommendation system.
        - **Learn More About Us:** Get to know the team behind this application and our mission.

        ### How to Get Started:

        1. **Navigate Using the Sidebar:** Use the sidebar to access different sections of the application:
            - **Information:** Learn more about the purpose and functionality of the application.
            - **EDA:** Explore data visualizations and statistics about anime categories.
            - **Recommendation:** Enter your preferences to get personalized anime recommendations.
            - **Feedback:** Share your feedback to help us enhance the app.
            - **About Us:** Find out more about the team and the project.

        2. **Enter Preferences:** 
            - For anime recommendations, provide either a User ID (for collaborative filtering) or up to 3 anime titles (for content-based filtering).
        
        3. **Receive Recommendations:** View a list of recommended anime based on your input, complete with images and details.

        ### Get the Most Out of the App:

        - Make sure to enter anime titles exactly as they appear in our dataset.
        - Explore the EDA section to understand trends and patterns in anime data.
        - Provide feedback to help us continuously improve the recommendation system.

        Enjoy discovering new anime and exploring our app!
        """
    )
