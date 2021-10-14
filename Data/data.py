#from firebase import Firebase
import os
import json
import firebase_admin
from firebase_admin import credentials , db
from dotenv import load_dotenv
load_dotenv()

cred_obj = firebase_admin.credentials.Certificate(os.getenv('pathadminsdk'))

default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':os.getenv('databaseURL')
	})

def setd():
    ref = db.reference("/")
    with open("book_info.json", "r") as f:
        file_contents = json.load(f)
    ref.set(file_contents)

def retrive():
    ref = db.reference("/Book1/Author/")
    best_sellers = ref.get()
    print(best_sellers)

retrive()    