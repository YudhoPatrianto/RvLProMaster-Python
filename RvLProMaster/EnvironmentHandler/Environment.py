# Load Library
from dotenv import load_dotenv as LoadEnv
import os

# Loads Environment
LoadEnv()

# Select Environment
GeminiAPI_KEY = os.getenv('GEMINI_KEY')
GITHUB_ENV = os.environ.get('GITHUB_ENV')
TelegramBOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
MONGODB = os.getenv('MONGODB_URL')