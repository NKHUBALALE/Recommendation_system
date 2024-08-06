# Anime Recommendation System

## Overview

The Anime Recommendation System is a web application developed using Streamlit, designed to help users discover new anime based on their preferences. It leverages machine learning algorithms to provide personalized recommendations, using data about various anime and user ratings.

## Features

- **Home**: Welcome page with an overview of the application.
- **Information**: General information about the recommendation system and the methodologies used.
- **EDA (Exploratory Data Analysis)**: Visualizations and analysis of anime data, including genre distribution and rating patterns.
- **Recommendation**: Personalized anime recommendations based on user input.
- **Feedback**: Option for users to provide feedback on the application.
- **About Us**: Information about the development team and the project's mission.

## Technologies Used

- **Python**: Programming language used for development.
- **Streamlit**: Framework for building the web application.
- **Pandas**: Library for data manipulation and analysis.
- **Scikit-Surprise**: Library for building and evaluating recommender systems.
- **Pickle**: For serializing and deserializing Python objects.
- **NumPy**: Library for numerical operations.

## Installation

To set up the project, follow these steps:

1. **Fork the Repository**

   Fork the repository to your GitHub profile.

2. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Recommendation_system.git
   cd Recommendation_system

3. **Create a Virtual Environment**

  It is recommended to use Python 3.10 to avoid potential library conflicts (e.g., with Scikit-Surprise).

4 Activate the Virtual Environment

  On Windows:

  ```bash
  venv\Scripts\activate
  ```
5. Install Required Packages

  Use the requirements.txt file to install the necessary packages.

  ```bash
  pip install -r requirements.txt
  ```
6 Run the Application

  ```bash
  streamlit run app.py
  ```