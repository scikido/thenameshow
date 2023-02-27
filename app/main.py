import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import credentials , db, initialize_app
from flask_login import LoginManager , login_user, logout_user , login_required
from flask import Flask , render_template , session
from jinja2.utils import pass_environment

load_dotenv()
app=Flask(__name__)

cred_obj = firebase_admin.credentials.Certificate({
  "type": "service_account",
  "project_id": "thenameshow-b5111",
  "private_key_id": "04ad6338d04ac045de746df1ea0d79e64c7e196b",
  "private_key": os.getenv("PRIVATE_KEY"),
  "client_email": os.getenv('cliend_mail'),
  "client_id": "109000000000000000000",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.getenv('client_x509_cert_url')
})

flaskapp = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://thenameshow-b5111-default-rtdb.firebaseio.com/'
	})


def retrive(path):
    ref = db.reference(path)
    content = ref.get()
    return content

def setd():
    ref = db.reference("/")
    with open('Data/blogload.json', "r") as f:
        file_contents = json.load(f)
    ref.set(file_contents)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/blogs')
def blog():
    return render_template('blog.html')

@app.route('/musings')
def quotes():
    return render_template('musings.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog1')
def blogs():
    return render_template('blog_1.html')

app.jinja_env.globals.update(retrive=retrive )

def callback():
    pass

#setd()
#print(retrive("Content/Poems/poem1/Body/"))