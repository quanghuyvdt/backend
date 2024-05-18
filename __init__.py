from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient


app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://localhost:27017')
db = client['midterm']