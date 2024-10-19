import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Getting API key from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
