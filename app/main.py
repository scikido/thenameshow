import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import credentials , db, initialize_app
from flask_login import LoginManager , login_user, logout_user , login_required
from flask import Flask , render_template , session

load_dotenv()
app=Flask(__name__)

cred_obj = firebase_admin.credentials.Certificate(os.getenv('pathadminsdk'))

flaskapp = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':os.getenv('databaseURL')
	})



def retrive(path):
    ref = db.reference(path)
    content = ref.get()
    return content


def setd():
    ref = db.reference("/")
    with open("Data//blogload.json", "r") as f:
        file_contents = json.load(f)
    ref.set(file_contents)


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