import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import credentials , db, initialize_app
from flask_login import LoginManager , login_user, logout_user , login_required
from flask import Flask , render_template , session

load_dotenv()
app=Flask(__name__)

cred_obj = firebase_admin.credentials.Certificate({
  "type": "service_account",
  "project_id": "the-name-show",
  "private_key_id": "7e8bf3907bcf49269d90e43ae41f3bf85c51746a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC67dpTDPJOIfGt\nu+88qBccrz+CwsGxTf9/C/dgJvgFxrIEaitYXa6L7DNyirXJgFVeRBMxEU/AnK2m\nP5JX9VbStg/zkz50XQCTZX3okHFlTPRQ1uNes3+qeuvRCYHCOntsqbn3+P86u/xX\n23xjVpWblt6xZUxeBDJvOQPiLnrdMdjjh35rYz+x9WlpXTHmtdnxUGjMctxC9kUi\nJftL9QzQNWq3ctYiv1DttLxcabHRjUdR7htqLq9dv1smVnVtlPlH6MNVQjQCqoZN\nsIhifPdWdWMB22dmvyFlSSBQqgNhUzjaTKgvkounFQyIJo6GCXq5ETMgfMudhsxG\nqlua7BQDAgMBAAECggEANKGo0a55AOfMyOp76zu2ujRbsQEOEVKRSB/B6JhASDwQ\nPm74QlqqPSplt+/3TENuheqr7qpdprFWsVL/7PUem5h4eE/yi0fuVBIE9/jHfMrE\nlYhTn4Pxw7n1cLd5Cgt2WfuV6Yx5rHtmiwQ5Cy1DVXoOvKr1bBlJbAiFH+ePX3zg\nKezVzQ7BMW/cpUTvE1URtb+RornKtyWTATdeIBs79VFRLCDCgOBPO0Ml/QAiBpN1\nOJOCYC7FemaRxksgLImG594xwMhrUClEWM7TIIOWERaYx1bxHZnra39E5Cn/259G\nWqPX3dFY0R2bVSwG0neFwKp298lENz9PRkHKrMC09QKBgQDyefrUQzvdOu+6ijO3\nZ9yFKuiLt62G5q+RPxuK67bDi2XBaYtzXD47LtQ8Xk9vDxU4liHBiy6WKufXtze0\nEC+GZk3FHP7yR7hAmcLjsGWC+l50dMgDApueTQswEegpoMnoJzhhNf5GckiR1efZ\nmfYRiWlDpb35t2AgE95SlL0qTwKBgQDFWsf8BMheZ389vue2qTdrnP8bUgCaBypZ\npJdXCxqU+4ONO2zjaIHYs47RBoBT0/o98cphtsBeU+F+MRmoQ/akaTXOJ85w3wQp\neCUqc7FaCExuA61Iu9wwNz8a+fB/8o/u5lbCPsw/dMqH4Q5SuA830l/xuTbd7x6x\n8rNiEDqyDQKBgD8AOo/UOEWu/oK1TeKldcKT93/15Xxbi9ptTza1L/N20KWEStta\naEDwVeyphHIStSzStUqYYy5ZT4vY6vw6CF8fTa2dbxB8Wf9O9Dg8qONzMf+IKD+/\n+bcTxYhj3rKSOGO9bQS1BrA/GWPq9CaxviGoVlVhRw8O+kbbYrSKOOw5AoGACeCR\nQbu7i34CkESNtEajz278FZH1FcBmDjZ+nIyht/MekmL3ACqq1P2nmC6LHabuT0ta\npalP12i7UGWEszczkObzGm5DlsKSosCwm39O0QK5UIg+k/VS/9bEAcWgk8bADWTZ\n0r7x2fsuZ76LyPgNSu3sf1yVsmXVU3KiJ7ZIOcECgYAdfvdgVFYvaO+iVRuUG3V+\nzeqI3rFjH7tXvp1FvfZTnaO6j4h18OJXqFqd3fsX79876RKyYaggwx0G8u2IEpvK\nxlD3yysDNSZnLBOEMe5bWT99ie7+8fz69mYU9keawM/x+HprCIcF62t6GphvtWfr\ndhudqeOh+x67jNhxnK0/lg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ug7ak@the-name-show.iam.gserviceaccount.com",
  "client_id": "105021080401059024333",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ug7ak%40the-name-show.iam.gserviceaccount.com"
})

flaskapp = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://the-name-show-default-rtdb.firebaseio.com/'
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