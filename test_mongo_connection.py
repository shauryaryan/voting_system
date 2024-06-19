from pymongo import MongoClient
from urllib.parse import quote_plus

# URL-encode the username and password
username = quote_plus('shauryaryann')
password = quote_plus('Street16@@')

# MongoDB Atlas connection string with encoded credentials
mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.jbfcntv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client.get_database('voting_system')

print("Connected to MongoDB Atlas!")
print("Database name:", db.name)



