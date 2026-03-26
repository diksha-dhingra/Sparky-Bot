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
        return "🔄 Conversation cleared! Let's start fresh. What's on your mind?"

    elif cmd == "/about":
        return ABOUT_MESSAGE

    return "❓ Unknown command. Type */help* to see available commands."