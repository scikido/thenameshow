import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import credentials , db
from flask_login import LoginManager , login_user, logout_user , login_required


from flask import Flask , render_template , session
load_dotenv()
app=Flask(__name__)



def retrive():
    ref = db.reference("/Book1/Author/")
    best_sellers = ref.get()
    print(best_sellers)

@app.route('/')
def hello():
    return render_template('index.html')


'''@app.route('/example')
def exampl():
    return render_template('exampleblog.html')'''


@app.route('/blogs')
def blog():
    return render_template('blog.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/blog1')
def blogs():
    return render_template('blog_1.html', blog=os.getenv('xyz'))

def callback():
    pass

#retrive()