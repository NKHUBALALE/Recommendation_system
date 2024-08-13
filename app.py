import streamlit as st
import pandas as pd
from scripts_for_pages import home, information, eda, feedback, about_us
from scripts_for_pages.recommendations import get_recommendations, fetch_anime_image, best_svd_model, anime_data, merged_df
from styles.styles import set_background_image, apply_custom_styles

def main():
    """Main function for the Streamlit app"""
    
    # Apply background image and custom styles
    set_background_image('images/image.png', brightness=0.6)  # Update the path to your image
    apply_custom_styles()
    
    # Create a header and subheader
    st.title("Anime Recommendation System")
    st.subheader("Explore and discover new anime")
    
    # Sidebar navigation
    options = ["Home", "Information", "EDA", "Recommendation", "Feedback", "About Us"]
    selection = st.sidebar.selectbox("Choose Option", options)
    
    # Page routing
    if selection == "Home":
        home.display()
    elif selection == "Information":
        information.display()
    elif selection == "EDA":
        eda.display()
    elif selection == "Recommendation":
        st.info("Anime Recommendations")
        user_id = st.text_input("Enter User ID", '')

        if user_id:
            # Add a radio button to select the recommendation method
            recommendation_method = st.radio(
                "Choose Recommendation Method",
                ("Collaborative Filtering", "Content-Based Filtering")
            )

            if recommendation_method == "Collaborative Filtering":
                recommendations = get_recommendations(user_id, best_svd_model, anime_data, merged_df)
            else:
                st.write("Content-Based Filtering is not yet implemented.")
                recommendations = pd.DataFrame()  # Create an empty DataFrame

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
                            f"<div class='anime-title'>{title}</div> - You are likely to give a rating of {row['predicted_rating']}",
                            unsafe_allow_html=True
                        )
                        st.image(image_url, caption=title, use_column_width=True)  # Use column width scaling
                    else:
                        st.markdown(
                            f"<div class='anime-title'>{title}</div> - You are likely to give a rating of {row['predicted_rating']}",
                            unsafe_allow_html=True
                        )
    elif selection == "Feedback":
        feedback.display()
    elif selection == "About Us":
        about_us.display()

if __name__ == "__main__":
    main()
