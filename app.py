from flask import Flask
from controllers.user_controller import UserController

app = Flask(__name__)

# Initialize the user controller
user_controller = UserController()

# Create API routes for CRUD operations

@app.route('/users', methods=['POST'])
def create_user():
    return user_controller.create_user()

@app.route('/users', methods=['GET'])
def get_users():
    return user_controller.get_users()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return user_controller.update_user(user_id)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_controller.delete_user(user_id)

if __name__ == '__main__':
    app.run(debug=True)
