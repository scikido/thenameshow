import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask , render_template

app=Flask(__name__)
def login_required(function):
    pass

@app.route('/')
@login_required
def hello():
    return render_template('index.html')
 
if __name__=="__main__":
    app.run(debug=True)
