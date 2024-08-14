import streamlit as st
import pandas as pd
from scripts_for_pages import home, information, eda, feedback, about_us
from scripts_for_pages.recommendations import get_recommendations, get_content_based_recommendations, fetch_anime_image, best_svd_model, anime_data, merged_df, tfidf_matrix, feature_names
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
        
        # Choose Recommendation Method
        recommendation_method = st.radio(
            "Choose Recommendation Method",
            ("Collaborative Filtering", "Content-Based Filtering")
        )

        if recommendation_method == "Collaborative Filtering":
            user_id = st.text_input("Enter User ID", '')
            if user_id:
                try:
                    recommendations = get_recommendations(user_id, best_svd_model, anime_data, merged_df)
                    if not recommendations.empty:
                        st.write("Based on the information we have, we think these are the anime you would love and how you'd rate them:")
                        recommendations = recommendations[['anime_id', 'predicted_rating']]
                        for index, row in recommendations.iterrows():
                            anime_id = row['anime_id']
                            title, image_url = fetch_anime_image(anime_id)
                            if not title or not image_url:
                                title = anime_data.loc[anime_data['anime_id'] == anime_id, 'name'].values[0]
                                image_url = None
                            if image_url:
                                st.markdown(
                                    f"<div class='anime-title'>{title}</div> - {'You are likely to give a rating of ' + row['predicted_rating'] if 'predicted_rating' in row else 'Rated: ' + str(row['rating'])}",
                                    unsafe_allow_html=True
                                )
                                st.image(image_url, caption=title, use_column_width=True) 
                            else:
                                st.markdown(
                                    f"<div class='anime-title'>{title}</div> - {'You are likely to give a rating of ' + row['predicted_rating'] if 'predicted_rating' in row else 'Rated: ' + str(row['rating'])}",
                                    unsafe_allow_html=True
                                )
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        
        elif recommendation_method == "Content-Based Filtering":
            user_animes = st.text_input("Enter up to 3 Anime Titles (comma separated)", '').split(',')
            user_animes = [anime.strip() for anime in user_animes if anime.strip()]
            if user_animes:
                try:
                    recommendations = get_content_based_recommendations(user_animes, anime_data, tfidf_matrix, feature_names)
                    if not recommendations.empty:
                        st.write("Based on the information we have, we think these are the anime you might enjoy:")
                        recommendations = recommendations[['anime_id', 'name', 'rating']]
                        for index, row in recommendations.iterrows():
                            anime_id = row['anime_id']
                            title, image_url = fetch_anime_image(anime_id)
                            if not title or not image_url:
                                title = anime_data.loc[anime_data['anime_id'] == anime_id, 'name'].values[0]
                                image_url = None
                            if image_url:
                                st.markdown(
                                    f"<div class='anime-title'>{title}</div> - {'Rated: ' + str(row['rating'])}",
                                    unsafe_allow_html=True
                                )
                                st.image(image_url, caption=title, use_column_width=True)
                            else:
                                st.markdown(
                                    f"<div class='anime-title'>{title}</div> - {'Rated: ' + str(row['rating'])}",
                                    unsafe_allow_html=True
                                )
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    elif selection == "Feedback":
        feedback.display()
    elif selection == "About Us":
        about_us.display()

if __name__ == "__main__":
    main()
