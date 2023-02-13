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
db.child().push({
    "Content": {
        "Poems": {
            "poem1": {
                "Title": "My Scars",
                "Body": "The wind was flowing  \n The trees were talking The oceans were waving \n The clothes on the rope were chuckling \n The Thunder was roaring \n The rain was dancing \n And the boy was happy thinking the  \n Moon was singing along the stars as \n the wind flowed across his scars "
            },
            "poem2": {
                "Title": "Silent Tears",
                "Body": "Days will pass And turn to years And I'll always remember you, With silent tears."
            }
        },
        "Blogs": {
            "Two Days of Freedom": {
                "Chapter1": {
                    "Title": "Yash Going Missing",
                    "Body": "Aisha was cleaning kitchen until she realized that Yash has not woke up early today for his usual jogging at 6'o clock. She called Yash from kitchen, but no response. She assumed he must be tired today, so she started cooking breakfast."

                }
            }
        },
        "Musings": {
            "Author": "SciKido",
            "1": "My demons come free, With the angels in me.\nHow can you love just a part of me?",
            "2": "I just can't stop staring at the sky, \nquestioning myself were the stars still glitering when then world was being formed.",
            "3": "I know I won't talk to you, \nBut never talking to you is the thing I will regret forever",
            "4": "I know we were'nt perfect, \nBut just a little longer would've made us perfect.",
            "5": "Life is very Boring, \nif you make it!",
            "6": "You have to learn to play fire with fire \nin accordance to live satisfyingly "
        }
    },
    "About": {
        "Thenameshow": "We are team SCI. A youth trying to provide sustainable services to people. You will find here bunch of free services like listening to music with your friends in a session without using any app. Morever, you will find spicy blogs and musings to entertain you. The novel section gets updated every two weeks to give you the best experience. Do review and rate us here. Suggestions are accepted at via mail."
    }
})
# ccc= db.child("About").get()
# print(ccc.val())
# path="Content/Musings/1"


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