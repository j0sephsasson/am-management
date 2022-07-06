import os
import warnings
from dotenv import load_dotenv
warnings.filterwarnings('ignore')

import pickle, pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

## init env variables
load_dotenv()

## init flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# default page of our web-app
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('test.html')

# index
@app.route('/enter', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)