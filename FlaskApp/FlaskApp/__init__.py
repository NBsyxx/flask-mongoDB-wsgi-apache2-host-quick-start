# System path 
import sys

# System extensions
from re import X
sys.path.insert(0, "/usr/local/lib/python3.8/dist-packages") # path set
import os
import pickle
import math
import time

# Database extensions 
import pymongo
from pymongo import MongoClient


# Simple backup data_entries to MongoDB
def backup(data_entries):
    cluster = MongoClient("#identifications",connect=False)
    db = cluster["#clustername"]
    collection = db["#clustercollection"]

    print("connected ",cluster)

    post = {}
    # collection.insert_one(post)

# Initialize the FlaskApp
app = Flask(__name__)


# Route to default page 
@app.route('/',methods=['GET', 'POST'])
def hello():
    return render_template('index.html')


# Route to result page GET -> POST 
@app.route('/methods',methods=['GET', 'POST'])
def calculate():
        return render_template('outcome.html')


# This part is unnecessary cause we are virtual hosting the things 
if __name__ == "__main__":
    app.run(debug=True)
