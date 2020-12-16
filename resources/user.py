from flask import request
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password, check_password
from Models.user import User
from flask_jwt_extended import jwt_optional, get_jwt_identity


class UserListResource(Resource):

    def post(self):
        json_data = request.get_json()

        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')

        if User.get_by_username(username):
            return {'message': 'username already'}, HTTPStatus.BAD_REQUEST

        if User.get_by_email(email):
            return {'message': 'email already exists'}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)

        user = User(username=username, email=email, password=password)
        user.save()

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        return data, HTTPStatus.CREATED

class UserResource(Resource):

    @jwt_optional
    def get(self, username):
        user = User.get_by_username(username=username)

        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user == user.id:
            data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }
        else:
            data = {
                'id': user.id,
                'username': user.username
            }
        return data, HTTPStatus.OK