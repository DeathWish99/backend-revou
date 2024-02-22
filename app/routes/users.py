# Defining Routes and API Endpoints
from flask import Blueprint, Flask, request, jsonify

example = Blueprint('example', __name__)

# Sample data (for demonstration purposes)
users = [
    {"id": 1, "username": "john_doe", "email": "john@example.com"},
    {"id": 2, "username": "alice_smith", "email": "alice@example.com"},
]

# GET: Retrieve all users
@example.route('/getusers', methods=['GET'])
def get_users():
    return jsonify(users)

#Get BY ID
@example.route('/getusers/<int:user_id>', methods=['GET'])
def get_users_byid(user_id):
    userid = user_id
    return jsonify(users)

# POST: Create a new user
@example.route('/postusers', methods=['GET','POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "username": data.get('username'),
        "email": data.get('email')
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT: Update an existing user
@example.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user['username'] = data.get('username')
            user['email'] = data.get('email')
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# DELETE: Remove a user
@example.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"})
    return jsonify({"message": "User not found"}), 404