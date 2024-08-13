# styles/styles.py

import streamlit as st
import base64

def set_background_image(image_path, brightness=0.6):
    """Function to set background image"""
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_image});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            filter: brightness({brightness});
        }}
        .stApp > div {{
            background-color: rgba(0, 0, 0, 0.6);  /* Darken the background for better text visibility */
            padding: 10px;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def apply_custom_styles():
    """Apply custom CSS styles"""
    anime_style = """
    <style>
    body {
        background-color: #f0f0f0;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #333;
    }
    h1 {
        color: #ff6699;
        text-shadow: 2px 2px #ffb3d9;
    }
    h2, h3, h4 {
        color: #ff6699;
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
        background-color: #ff6699;
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
        border: 2px solid #ff6699;
        border-radius: 5px;
        padding: 5px;
    }
    .stTextArea>div>div>textarea {
        border: 2px solid #ff6699;
        border-radius: 5px;
        padding: 5px;
    }
    .anime-title {
        font-size: 20px; /* Adjust font size as needed */
        color: #ff6699; /* Same color as the heading */
        font-weight: bold;
    }
    </style>
    """
    st.markdown(anime_style, unsafe_allow_html=True)
