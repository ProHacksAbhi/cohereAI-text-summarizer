import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# Load API Key 
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

# Initialize Cohere Client V2  
co = cohere.ClientV2(api_key=cohere_api_key)

# Streamlit UI 
st.title("Text Summarization with Cohere")
st.write("This uses Coheres API summarized text. Enter the text you want to summarize below.")

# Text Input ("height equals 300")
user_input = st.text_area("Enter text:", height=300)

# Logic ( flow: Button -> Input Check -> Spinner -> Try/Except)
if st.button("Summarize"):
    if user_input:
        with st.spinner("Summarizing..."):
            try:
                # Prepare the message ( "Generate a concise summary...")
                message = f"Generate a concise summary for the following text: {user_input}"
                
                # Call Chat Endpoint ( "change summarize endpoint to chat endpoint")
                response = co.chat(
                    model="command-r-plus",
                    messages=[{"role": "user", "content": message}]
                )
                
                # Extract Summary ("response.message.content[0].text")
                summary = response.message.content[0].text
                
                # Display Result
                st.subheader("Summarized Text")
                st.write(summary)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to summarize.")