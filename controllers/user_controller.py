from flask import request, jsonify
from models.user_model import UserModel

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def create_user(self):
        data = request.get_json()
        result = self.user_model.create_user(data['name'], data['email'])
        if result:
            return jsonify({'message': 'User created successfully'}), 201
        else:
            return jsonify({'message': 'Failed to create user'}), 500

    def get_users(self):
        users = self.user_model.get_users()
        return jsonify(users), 200

    def update_user(self, user_id):
        data = request.get_json()
        result = self.user_model.update_user(user_id, data['name'], data['email'])
        if result:
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            return jsonify({'message': 'Failed to update user'}), 500

    def delete_user(self, user_id):
        result = self.user_model.delete_user(user_id)
        if result:
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'message': 'Failed to delete user'}), 500
