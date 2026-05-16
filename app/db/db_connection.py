from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27018/"
client = MongoClient(MONGO_URL)

db = client["chromedb"]

chrome_collection = db["chromes"]
