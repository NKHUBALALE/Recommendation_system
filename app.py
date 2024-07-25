# Streamlit dependencies
import streamlit as st

# Custom CSS for anime style
anime_style = """
<style>
body {
    background-color: #f0f0f0;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    color: #333;
}
h1 {
    color: #ff6699; /* Updated color for the main title */
    text-shadow: 2px 2px #ffb3d9;
}
h2, h3, h4 {
    color: #ff6699; /* Updated color for subheaders */
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
    background-color: #ff6699; /* Updated button color */
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
    border: 2px solid #ff6699; /* Updated input border color */
    border-radius: 5px;
    padding: 5px;
}
.stTextArea>div>div>textarea {
    border: 2px solid #ff6699; /* Updated textarea border color */
    border-radius: 5px;
    padding: 5px;
}
</style>
"""

# Main function to build the Streamlit app
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

        # Placeholder for future visualizations (e.g., genre distribution, rating distributions)
        st.markdown("Visualizations will be added here.")

    # Building out the Recommendation page
    if selection == "Recommendation":
        st.info("Anime Recommendations")

        # Placeholder for user input and recommendations
        st.markdown(
            """
            This section will allow users to input their favorite anime and get personalized recommendations.
            """
        )

        # Example: Simple text input for favorite anime
        favorite_anime = st.text_input("Enter your favorite anime:", "")
        if st.button("Get Recommendations"):
            st.markdown(f"Recommendations based on {favorite_anime} will be displayed here.")

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
            This application was developed by Team_JB3, a group of data science students from the ExploreAI academy as a project to build a recommendation system for anime. It demonstrates the use of various recommendation algorithms to analyze and suggest anime.

            For more information or inquiries, please contact us at mm1_classification@sandtech.co.za.

            ---

            **Our Mission:**

            "We are here to innovate Africa and the world through data-driven insights, one anime at a time."
            """
        )

# Execute the main function
if __name__ == '__main__':
    main()
