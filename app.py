# Import the necessary libraries
from flask import Flask, request, render_template, send_file
from flask_cors import CORS
import requests
from bardapi import Bard

bard_token = ""

def get_questions(captions, question):
    bard = Bard(token=bard_token, timeout=30)
    prompt = captions + "\n\Answer in a single sentence. Don't add filler words. Just be precise.\n\n" + question
    response = bard.get_answer(prompt)['content']
    return response
    

# Create a Flask app
app = Flask(__name__, static_url_path='/static', template_folder='web/templates')

app.static_folder = 'static'

# Enable CORS for all origins
CORS(app)


# Define a GET endpoint
@app.route("/")
def index():
    return "Hello, world!"

@app.route("/update", methods=['GET', 'POST'])
def update():
    global bard_token
    new_token = bard_token
    if request.method == 'POST':
        print(request.form['new_token'])
        new_token = request.form['new_token']
        bard_token = new_token
        return render_template("./success.html", token=new_token)
    return render_template("./update.html", token=new_token)

