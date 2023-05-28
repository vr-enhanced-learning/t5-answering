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
