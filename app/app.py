import pyrebase
from flask import * 

config = {
  "apiKey": "AIzaSyCBxyBzNf13Vu73AQySWepeHIbozqst1J8",
  "authDomain": "the-name-show.firebaseapp.com",
  "databaseURL": "https://the-name-show-default-rtdb.firebaseio.com",
  "projectId": "the-name-show",
  "storageBucket": "the-name-show.appspot.com",
  "messagingSenderId": "128897615695",
  "appId": "1:128897615695:web:1282a2102eff8a8b01273a"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

ccc= db.child("").child("Content").child("Musings").child("3").get()
path="/-NO6mYJ127KmQ0z7zthl/Content/Musings/1"
print(ccc.val())

def retrive(path):
    pass

app = Flask(__name__)
@app.route('/')
def basic():
    return render_template('index.html')


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


# if __name__ == '__main__':
#     app.run(debug=True)