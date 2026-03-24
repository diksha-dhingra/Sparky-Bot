from personality import HELP_MESSAGE, ABOUT_MESSAGE, WELCOME_MESSAGE

COMMANDS = ["/help", "/reset", "/about", "/start"]


def is_command(message: str) -> bool:
    return message.strip().lower() in COMMANDS


def handle_command(message: str, sender: str, chat_sessions: dict) -> str:
    cmd = message.strip().lower()

    if cmd == "/start":
        return WELCOME_MESSAGE

    elif cmd == "/help":
        return HELP_MESSAGE

    elif cmd == "/reset":
        if sender in chat_sessions:
            del chat_sessions[sender]
        return "Chat reset ho gaya! Ab nayi baat shuru karo."

    elif cmd == "/about":
        return ABOUT_MESSAGE

    return "Unknown command. /help type karo."