import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
APP_ID = os.environ.get("NUTRITIONIX_ID")

