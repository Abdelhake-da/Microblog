from pymongo import MongoClient

USER_NAME = "***************"
PASSWORD = "**********"
client = MongoClient("mongodb+srv://"+USER_NAME+":"+PASSWORD+"@mictoblog-application.s9yuslt.mongodb.net/")

db = client.microblog.data
def get_element():
    return [e for e in db.find({})]

def insert_element(dict):
    if db.find_one(dict) is None:
        db.insert_one(dict)
    