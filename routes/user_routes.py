from flask import Flask, jsonify, request

from entities.user import User
from daos.user_dao import UserDao
from daos.user_dao_postgres import UserDaoPostgres

from services.user_service_impl import UserServiceImpl

from exceptions.exceptions import ResourceNotFoundError, InvalidCredentialsError

user_dao: UserDao = UserDaoPostgres()
user_service = UserServiceImpl(user_dao)

def user_routes(app: Flask):
    @app.post('/users')
    def create_new_user():
        new_user = User.from_json(request.json)
        result = user_service.add_user(new_user)
        return jsonify(result.json()), 201

    @app.get('/users')
    def get_all_users():
        all_users = user_service.get_all_users()
        return jsonify([user.json() for user in all_users]), 200

    @app.get('/users/<user_id>')
    def get_single_user(user_id: str):
        try:
            if not user_id.isnumeric():
                return "Invalid URI, user ID must be numeric", 400
            user = user_service.get_single_user(int(user_id))
            return jsonify(user.json()), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.put('/users/<user_id>')
    def update_user(user_id: str):
        if not user_id.isnumeric():
            return "Invalid URI, user ID must be numeric", 400
        try:
            updated_user = User.from_json(request.json)
            updated_user.user_id = int(user_id)
            result = user_service.update_user(updated_user)
            return jsonify(result.json), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.delete('/users/<user_id>')
    def delete_user(user_id: str):
        if not user_id.isnumeric():
            return "Invalid URI, user ID must be numeric"
        try:
            user_service.delete_user(int(user_id))
            return "User successfully deleted", 205
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.post('/users/login')
    def login():
        if 'username' in request.json and 'password' in request.json:
            try:
                username = request.json['username']
                password = request.json['password']
                user_type, id = user_service.login(username, password)
                return jsonify({'userType':user_type, 'userId': id}), 200
            except InvalidCredentialsError as e:
                return str(e), 422
        else:
            return "Ivalid JSON Body", 400