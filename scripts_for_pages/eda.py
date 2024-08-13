import streamlit as st

def display():
    """EDA page content"""
    st.title("Exploratory Data Analysis")

    st.info("Exploratory Data Analysis")

    st.markdown(
        """
        Overview and Introduction:

        - The purpose of the Exploratory Data Analysis (EDA) is to examine the distribution of anime data, such as genres, ratings, and popularity.
        - Understanding the data helps in identifying patterns and potential biases, which are critical for developing accurate recommendation models.
        """
    )

    st.markdown(
        """
        ### Distribution of Anime Genres

        The following visualization provides insights into the distribution of anime across various genres. This helps in understanding genre popularity and diversity.
        """
    )
    st.image('images/anime by genre.png', caption='Distribution of Anime by Genre', use_column_width=True)

    st.markdown(
        """
        ### Balance of Anime Type

        This visualization illustrates the data balance before and after resampling techniques were applied. It is important to visualize data imbalance as it can significantly impact the performance of machine learning models.
        """
    )
    st.image('images/image copy.png', caption='Data Balance Visualization', use_column_width=True)

    st.markdown(
        """
        ### Distribution of How the Genre Was Watched
        """
    )
    st.image('images/most watched anime.png', caption='Distribution of How the Genre Was Watched', use_column_width=True)
