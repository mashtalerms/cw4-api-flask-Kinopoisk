from flask import request
from flask_restx import Resource, Namespace

from project.dao.model.userModel import UserSchema
from project.helpers.decorators import auth_required
from project.implemented import user_service, auth_service, movie_service, user_movie_service

user_ns = Namespace('user')
user_schema = UserSchema()


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = auth_service.get_email_from_token(token)

        user = user_service.get_by_email(email)
        user_dict = user_schema.dump(user)
        return user_dict, 200

    @auth_required
    def patch(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = auth_service.get_email_from_token(token)

        updated_data = user_schema.dump(request.json)
        user_service.update(updated_data, email)
        return "", 200


@user_ns.route('/password/')
class UserPasswordView(Resource):
    @auth_required
    def put(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = auth_service.get_email_from_token(token)

        passwords = request.json
        user_service.update_password(passwords, email)
        return "", 200


### Задание со звездочкой

@user_ns.route('/favorites/movies/<int:mid>/')
class UserMovieView(Resource):
    @auth_required
    def post(self, mid):
        print(mid)
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        user_id = auth_service.get_user_id_from_token(token)
        print(user_id)
        movie = movie_service.get_one(mid)
        print(movie.title)

        user_movie_service.add_favorite_movie(user_id, movie.id)

        return "", 200

    def delete(self, mid):
        pass