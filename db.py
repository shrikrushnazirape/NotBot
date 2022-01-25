from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://shrikrushna:"+"pass@123" + "@cluster0.eghoa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# client = pymongo.MongoClient(CONNECTION_STRING)
# db = client.get_database('notbot')
# user_collection = pymongo.collection.Collection(db, 'Chats')



client = pymongo.MongoClient(CONNECTION_STRING)
db = client.notbot
