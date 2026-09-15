import os

# For local use you may set these environment variables.
# Do not commit real bot credentials to a public repository.
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ALLOWED_CHAT_ID = int(os.getenv("ALLOWED_CHAT_ID", "0"))
