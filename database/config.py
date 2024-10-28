from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.get_database('lap')
collection = db.get_collection('laptops')
owner_collection = db.get_collection('owners')
user_collection = db.get_collection('users')

shop_collection = db.get_collection("shops")