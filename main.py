import cohere

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

co = cohere.ClientV2(api_key)
response = co.chat(
    model="command-r-plus", 
    messages=[{"role": "user", "content": "hello world!"}]
)
print(response.message.content)
