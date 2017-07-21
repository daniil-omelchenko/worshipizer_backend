from pymongo import MongoClient
import pymongo

import config


client = MongoClient(config.MONGODB_URI)
db = client[config.DATABASE]

song = db['song']
song.create_index([('metaData.title', pymongo.TEXT), ('source', pymongo.TEXT)])
