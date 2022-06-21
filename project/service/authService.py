import calendar
import datetime

import jwt
from flask import current_app
from flask_restx import abort

from project.service.userService import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)
        if user is None:
            raise abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "email": user.email
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(
            data,
            current_app.config.get('JWT_SECRET'),
            algorithm=current_app.config.get('JWT_ALGORITHM'))

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(
            data,
            current_app.config.get('JWT_SECRET'),
            algorithm=current_app.config.get('JWT_ALGORITHM'))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(
            jwt=refresh_token,
            key=current_app.config.get('JWT_SECRET'),
            algorithms=[current_app.config.get('JWT_ALGORITHM')])
        email = data.get('email')

        return self.generate_tokens(email, None, is_refresh=True)

    def get_email_from_token(self, token):
        data = jwt.decode(
            token,
            current_app.config.get('JWT_SECRET'),
            algorithms=[current_app.config.get('JWT_ALGORITHM')])
        email = data.get('email')
        return email

    def get_user_id_from_token(self, token):
        data = jwt.decode(
            token,
            current_app.config.get('JWT_SECRET'),
            algorithms=[current_app.config.get('JWT_ALGORITHM')])
        id = data.get('id')
        return id
