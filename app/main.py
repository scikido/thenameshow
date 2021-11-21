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
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCBpfez3++qhtbB\nxDKCFTFpZxoWi9MV06c9z/JEuz0aWxD/gjz0x08JpMkzflc7BUWGC8d/p7xq4xKT\n5VF4BcXJ6Ygj9n3iFA8HObzg+KnMHi6o6zb5rX4wV1w8bnmlSZmlAbr7tXk7M1w1\nUrrC59TPM2lHE8KgEAmiLaveoVjQ5GAakL3XGQecJkXX8iRtuU5IkodvVhul/rzQ\nKmAZvN5JSajtHXGDlyk7TUiqoRbkMyv81pqP10dxZfQ19eM5qeal53+SvRAFufdl\nwj8EwaHboJp44JJm1hD3wZeWgacLDvPOeAW4Dcm2gvkrqUc2nByikV8CiYU7I1mO\np51aarMlAgMBAAECggEACbJFf9z4OktCZZSMaIE4RFdTMqt7eo7tW6ihSHWugLmd\n4FY3w+DiLuj1qVXCJWZkCD36Sjhb1ays94W3nZ/k5pCCP5pQWOfCJfqx/ytp25vI\nRpbs8iiBHxFxkw16KJwEEzy5ZNjyO7TAKTbKRAh9uI9ySMAYFsuMROZgi9KKZ3kJ\n3K3u6oCFjWfQShC26JJhOCVRwEcfLKT3FzuBVrYdpYbeLUvl6CXRs8eHnttZzR6m\nlGINnuU0pVuI37EtqBVTg9qjShr+mQaadSvYinVfnYBYlf3xZmtOa54uHQz3TfS9\nrhaFrwKIeFlSQ5as1ArRcUoOWWKz30vnA18T0kSVAQKBgQC3BrpJwYQVaQJIDMDO\nFpcJ25Hs5CNUI7PmH8TtK1755CQfm3ifH3TPGkgt/0YSH/rWQyWZMDDHQzKUnMw8\nOAWdOzUa5J2w+DCS6negguZRlcO7JkUbkT39tesd8Khonqw3IqGzaAC88YFJti4W\njHnll2xmQpusIlSMHb3YH+1jgQKBgQC1VwPIfVZ6O9f89uHLRBTUSfsZUwhl58QM\ntaPpN+Ge8waUg3Cv0C8aj65OEYr7jLQHU/f7+HszZpKFvVrIFGs/Z9D3P3X0yscT\nYcMFl1p2A8uUfLPISuOvWORAZJWdbo0CWoGXkQndbiJ6r7GJ4uYZr243KpPsKRbB\n/RdAcc4RpQKBgDs6Wh50GSI0kSBvwBTxCn+OJnLagPRBeX4G2dtGJb4ILghsb2RO\n8aXzg1gfO7Wx06JyqEAicCaLgFrHQvBZ0LdI6a6CPOV/63gfmAbBVXchV+3APKzn\nG4B21lciAd2ZO3G8K0e7aEG8hXItGk0BuJCrp9CPzYCuu118YmsGKfQBAoGAaOkF\ndEkm7aKPi3bdHHavwj1murjx49rY7i1rvbIpooag6Oy+FcjQZ4J2ag32JR+6y36F\nuk2AITWXUS5CRfyiK1WJbHFXcZ6a25i0dhihKiN59NbMP/UrkjdQHfzTHfhmNdVc\noe40Edn0spvQj6AoVPXMQrgsSfVfiC0+9XahrE0CgYEAh3NIQ1KznyM3Yj7lBTlw\nsSplwP9psPk3U5Tk0YnjcKqqORPikOAkUfDH9T9tY5Xt8c+75KD4Cg43+lIND7ai\nIogBQWnxUo8j26Gr6bGMUNtzKigzLSGmxTdP5QkimOjLvOqkIGYXwssTYfbs1ktw\no8JPMGgNQAUMtQKV9ieEfUY=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-qc0cc@thenameshow-b5111.iam.gserviceaccount.com",
  "client_id": "114298377100827593646",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-qc0cc%40thenameshow-b5111.iam.gserviceaccount.com"
})

flaskapp = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://thenameshow-b5111-default-rtdb.firebaseio.com/'
	})

def playmusic(music):
    pass

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

@app.route('/blog1')
def blogs():
    return render_template('blog_1.html')

app.jinja_env.globals.update(retrive=retrive )

def callback():
    pass

#setd()
#print(retrive("Content/Musings/1/"))