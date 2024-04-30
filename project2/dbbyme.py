from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.project2
# specify a collection
collection = db.project2data

#simply opening the data
#going to to attempt to upload the data now
directory = "data"
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
        try:
            file_data = json.load(f)
            print(f, "successful upload")
            try:
                collection.insert_many(file_data)
                #print(file_data, "Succesful Upload")
            except Exception as e:
                print(e, "Error when importing into MONGO")
        except Exception as e:
                print(e)
                print(f, "There was a failure")

        