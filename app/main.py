import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import credentials , db, initialize_app
from flask_login import LoginManager , login_user, logout_user , login_required
from flask import Flask , render_template , session

load_dotenv()
app=Flask(__name__)

cred_obj = firebase_admin.credentials.Certificate(os.getenv('Data\the-name-show-firebase-adminsdk-ug7ak-7e8bf3907b.json'))

flaskapp = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':os.getenv('https://the-name-show-default-rtdb.firebaseio.com/')
	})



def retrive(path):
    ref = db.reference(path)
    content = ref.get()
    return content


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/blogs')
def blog():
    return render_template('blog.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/blog1')
def blogs():
    return render_template('blog_1.html')

app.jinja_env.globals.update(retrive=retrive )

def callback():
    pass


#retrive('Content/Poems/poem2/Body/')