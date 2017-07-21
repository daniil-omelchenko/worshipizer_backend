from pymongo import MongoClient

import config


client = MongoClient(config.MONGODB_URI)
db = client[config.DATABASE]

song = db['song']
