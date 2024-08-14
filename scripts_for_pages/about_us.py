import streamlit as st

def display():
    """About Us Page"""
    st.title("About Us")
    
    st.info("Learn More About Our Project and Team")

    st.markdown(
        """
        **Team JB3** is a group of data science enthusiasts from the ExploreAI academy. We embarked on this project as part of an unsupervised learning course with the aim of enhancing anime discovery through advanced recommendation algorithms.

        ### Project Goals

        Our goal is to provide personalized anime recommendations based on user preferences and behaviors. By employing both collaborative filtering and content-based techniques, we strive to help you find new favorites and enjoy a more tailored anime experience.


        ### Future Plans

        We are continuously working on improving the recommendation system and exploring new features. Stay tuned for updates and new functionalities that will make your anime discovery journey even more exciting.

        ### Acknowledgments

        Special thanks to our mentors, collaborators, and the ExploreAI academy for their guidance and support throughout this project.

        For any inquiries or if you are interested in collaborating with us, please contact us at [JB3unsupervised@sandtech.co.za](mailto:JB3unsupervised@sandtech.co.za).

        Thank you for your interest and support!
        """
    )

    # Optionally, add images or additional visual elements
    # st.image("path_to_image.jpg", caption="Team JB3")
