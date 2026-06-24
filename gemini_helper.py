import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        if hasattr(response, "text"):
            return response.text
        return "No response generated."
    except Exception as e:
        return f"ERROR: {str(e)}"
