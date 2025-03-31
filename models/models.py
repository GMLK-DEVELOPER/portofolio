from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

class Database:
    # Use environment variables for MongoDB connection in Docker
    _client_URL = MongoClient(
        f"mongodb+srv://{username}:{password}@portofolio.qktbtwr.mongodb.net/?retryWrites=true&w=majority&appName=portofolio"
    )
    db_name = _client_URL["PortfolyoFlask"]  # Database Name
