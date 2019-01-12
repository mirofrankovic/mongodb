import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI") # os library to set a constant called MONGODB_URI by using getenv method to read in environment variable
DBS_NAME = "mytestdb"
COLLECTION_NAME = "MyFirstMDB"

def mongo_connect(url):
    try: # block
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI) # coll our function

coll = conn[DBS_NAME][COLLECTION_NAME]

#update_one is a method
# first argumnet is nationality and is a search string
coll.update_one({'nationality': 'worldwide'}, {'$set': {'occupation': 'warior'}})

documents = coll.find({'nationality': 'worldwide'})

for doc in documents:
    print(doc)