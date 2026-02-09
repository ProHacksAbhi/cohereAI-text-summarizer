import cohere
import os
from dotenv import load_dotenv

# 1. Setup & Initialization
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(api_key=api_key)

# 2. Define the Function
def get_summary(text):
    """
    Sends text to Cohere API and returns the summary.
    """
    try:
        response = co.chat(
            model="command-a-03-2025", 
            messages=[{"role": "user", "content": f"Summarize this concisely: {text}"}]
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {e}"

# 3. Local Testing Block 
# Allows to run 'python main.py' to test the API without Streamlit
if __name__ == "__main__":
    test_text = "Cohere is a powerful AI platform for building LLM applications."
    print("Testing API...")
    print(get_summary(test_text))