import os
import google.generativeai as genai
from personality import SYSTEM_PROMPT

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# In-memory chat sessions — key: sender phone number, value: chat object
chat_sessions: dict = {}


def get_reply(sender: str, user_message: str) -> str:
    if sender not in chat_sessions:
        chat_sessions[sender] = model.start_chat(history=[])

    chat = chat_sessions[sender]

    try:
        response = chat.send_message(user_message)
        return response.text
    except Exception as e:
        print(f"Gemini error for {sender}: {e}")
        return "Kuch gadbad ho gayi, thodi der baad try karo."