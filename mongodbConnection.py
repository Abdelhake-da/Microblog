from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get("MICROBLOG_URI"))

db = client.microblog.data
def get_element():
    return [e for e in db.find({})]

def insert_element(dict):
    if db.find_one(dict) is None:
        db.insert_one(dict)
    