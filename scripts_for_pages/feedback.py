import streamlit as st

def display():
    """Feedback Page"""
    st.info("Feedback Form")

    feedback = st.text_area("Provide your feedback or suggestions here:")
    if st.button("Submit Feedback"):
        # Here, you would add code to save or process the feedback
        st.write("Thank you for your feedback!")
