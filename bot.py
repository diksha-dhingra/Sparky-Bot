import os
import google.generativeai as genai
from personality import SYSTEM_PROMPT

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash"
    system_instruction=SYSTEM_PROMPT
)

# In-memory chat history
chat_sessions: dict = {}

def get_reply(sender: str, user_message: str) -> str:
    if sender not in chat_sessions:
        chat_sessions[sender] = model.start_chat(history=[])

    # Keep history limited to 50 messages
    if len(chat_sessions[sender].history) > 50:
        chat_sessions[sender] = model.start_chat(
            history=chat_sessions[sender].history[-50:]
        )

    try:
        response = chat_sessions[sender].send_message(user_message)
        return response.text.strip()

    except Exception as e:
        print(f"Gemini error for {sender}: {e}")
        return "⚠️ Something went wrong on my end. Please try again in a moment!"