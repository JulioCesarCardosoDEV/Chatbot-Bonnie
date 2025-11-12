# gemini_config.py

import google.generativeai as genai

GEMINI_API_KEY = ""  # Chave do Gemini

def configure_gemini():
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel('models/gemini-1.5-flash')

def ask_gemini(model, prompt):
    response = model.generate_content(prompt)
    return response.text.strip()
