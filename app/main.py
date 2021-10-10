import os
from dotenv import load_dotenv
from flask_login import LoginManager , login_user, logout_user , login_required


from flask import Flask , render_template , session
load_dotenv()
app=Flask(__name__)



@app.route('/')
def hello():
    return render_template('index.html')



@app.route('/blogs')
def login():
    return render_template('blog.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

    
def logout():
    pass

def callback():
    pass