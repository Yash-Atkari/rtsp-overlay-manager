from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId

app = Flask(__name__)
CORS(app)  # Allows React frontend to connect

# Database Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/rtsp_stream_db"
mongo = PyMongo(app)

# Helper to format MongoDB objects for JSON
def format_overlay(o):
    return {
        "id": str(o["_id"]),
        "type": o["type"],
        "content": o["content"],
        "position": o["position"],
        "size": o["size"]
    }

# --- CRUD ENDPOINTS ---

@app.route('/')
def home():
    return "Backend is running! Use /overlays to see data."

@app.route('/overlays', methods=['POST'])
def create_overlay():
    data = request.json
    # Validation: Ensure type, content, position, and size
    result = mongo.db.overlays.insert_one(data)
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route('/overlays', methods=['GET'])
def get_overlays():
    overlays = mongo.db.overlays.find()
    return jsonify([format_overlay(o) for o in overlays]), 200

@app.route('/overlays/<id>', methods=['PUT'])
def update_overlay(id):
    data = request.json
    mongo.db.overlays.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Updated"}), 200

@app.route('/overlays/<id>', methods=['DELETE'])
def delete_overlay(id):
    mongo.db.overlays.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
