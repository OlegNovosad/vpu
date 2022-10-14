from pymongo import MongoClient

mongodb = "MONGODB URL"
client = MongoClient(mongodb)
database = client.get_database("default")
users_collection = database.get_collection("users")