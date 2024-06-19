# from flask import Flask, jsonify, request
# from pymongo import MongoClient
# import os
#
# app = Flask(__name__)
#
# # MongoDB Atlas connection string
# mongo_uri = "mongodb+srv://shauryaryann:Street16@@cluster0.jbfcntv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = MongoClient(mongo_uri)
# db = client.get_database('voting_system')
#
# @app.route('/')
# def home():
#     return "Welcome to the Fingerprint Voting System API!"
#
# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     users = db.users
#     users.insert_one(data)
#     return jsonify({'message': 'User registered successfully'}), 201
#
# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from urllib.parse import quote_plus
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# URL-encode the username and password
username = quote_plus('shauryaryann')
password = quote_plus('Street16@@')

# MongoDB Atlas connection string with encoded credentials
mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.jbfcntv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client.get_database('voting_system')
bcrypt = Bcrypt(app)


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/authenticate')
def authenticate_page():
    return render_template('authenticate.html')

@app.route('/vote')
def vote_page():
    return render_template('vote.html')

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

if __name__ == "__main__":
    from routes import *
    app.run(debug=True)






