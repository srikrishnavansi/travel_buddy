from langchain_google_genai import ChatGoogleGenerativeAI

def get_gemini_llm(google_api_key: str):
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=google_api_key,
        temperature=0.3,
    )
