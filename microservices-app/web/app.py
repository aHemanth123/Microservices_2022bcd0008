from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Connection
MONGO_HOST = os.getenv("MONGO_HOST", "db")
MONGO_PORT = 27018
MONGO_DB = "user_db"

client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
db = client[MONGO_DB]
users_collection = db["users"]

@app.route('/')
def index():
    return """
    <h1>Welcome to My Microservices App</h1>
    <p>Name: Hemanth Sai Manikanta Appari</p>
    <p>Roll Number: 2022BCD0008</p>
    <p>Short Bio: Passionate software developer working with microservices and cloud technologies.</p>
    """

# Endpoint to add a user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user = {"name": data["name"], "email": data["email"]}
    users_collection.insert_one(user)
    return jsonify({"message": "User added successfully"}), 201

# Endpoint to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {"_id": 0}))  # Exclude MongoDB's _id field
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
