from flask import request, abort
from flask_restx import Resource, Namespace

from project.dao.model.userModel import UserSchema
from project.implemented import auth_service, user_service

auth_ns = Namespace('auth')
user_schema = UserSchema()


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    def post(self):
        user_info = {
            'email': request.json.get('email'),
            'password': request.json.get('password')
        }

        if None in user_info.values():
            abort(400)

        data = user_schema.load(user_info)
        user = user_service.create(data)
        return "", 201, {"location": f"/users/{user.id}"}


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    def post(self):
        req_json = request.json

        email = req_json.get("email", None)
        password = req_json.get("password", None)

        if None in [email, password]:
            return "", 400

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
