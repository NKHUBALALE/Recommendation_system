import streamlit as st

def display():
    """Feedback Page"""
    st.title("Feedback Page")
    
    st.info("We value your feedback! Please provide your comments or suggestions below.")

    feedback = st.text_area("Provide your feedback or suggestions here:")
    optional_email = st.text_input("Optional: Enter your email address (if you'd like to be contacted):")

    if st.button("Submit Feedback"):
        if feedback.strip() == "":
            st.error("Feedback cannot be empty. Please provide your feedback or suggestions.")
        else:
            # Example: Save feedback to a file or send to a server
            # with open("feedback.txt", "a") as f:
            #     f.write(f"Feedback: {feedback}\nEmail: {optional_email}\n\n")
            
            # Optionally, you could use an API to submit the feedback
            # response = requests.post("http://example.com/feedback", data={"feedback": feedback, "email": optional_email})
            
            st.write("Thank you for your feedback! Your input helps us improve.")
            st.markdown(
                """
                ### Additional Information

                - If you have any further questions or need assistance, please contact us at [JB3unsupervised@sandtech.co.za](mailto:mm1_classification@sandtech.co.za).
                - Follow us on social media for updates and more information:
                  - [Twitter](https://twitter.com/yourprofile)
                  - [Facebook](https://facebook.com/yourprofile)
                  - [Instagram](https://instagram.com/yourprofile)
                """
            )
