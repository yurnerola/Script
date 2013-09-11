import pymongo
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

#client=MongoClient()
#The above code will connect on the default host and port. We can also specify the host and port explicitly, as follows:
#client=MongoClient("localhost",27017)
#Or use the MongoDB URI format:
client = MongoClient('mongodb://localhost:27017/')

db=client["test"]
collection=db.person
#print collection.find_one({"name":"jack"})

post={"author":"LiuBin","text":"My First blog post!","tags":["mongdb","python","pymongo"],"date":datetime.datetime.utcnow()}


posts=db.posts

post_id=posts.insert(post)

def get_exec_analyse(post_id):
	print posts.find({"_id" :post_id}).explain()["cursor"]
	print posts.find({"_id" :post_id}).explain()["nscanned"]

def get(post_id):
	print posts.find({"_id" :post_id})


get(post_id)
get_exec_analyse(post_id)


for post in posts.find():
	#print post
	pass
#print posts.find_one()
#print posts.count()



