import streamlit as st
import main  

st.title("Text Summarization App")
st.write("Powered by Cohere")

user_input = st.text_area("Enter text to summarize:", height=300)

# Interaction Logic
if st.button("Summarize"):
    if user_input:
        with st.spinner("Talking to Cohere..."):
            # Call the function from main.py
            summary_result = main.get_summary(user_input)
            
            # Check for errors returned by the function
            if "Error:" in summary_result:
                st.error(summary_result)
            else:
                st.subheader("Summary")
                st.write(summary_result)
    else:
        st.warning("Please enter some text first.")