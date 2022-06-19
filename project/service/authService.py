import calendar
import datetime

import jwt
from flask_restx import abort

from service.userService import UserService
from helpers.constants import secret, algo


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
        access_token = jwt.encode(data, secret, algorithm=algo)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=secret, algorithms=[algo])
        email = data.get('email')

        return self.generate_tokens(email, None, is_refresh=True)

    def get_email_from_token(self, token):
        data = jwt.decode(token, secret, algorithms=[algo])
        email = data.get('email')
        return email

    def get_user_id_from_token(self, token):
        data = jwt.decode(token, secret, algorithms=[algo])
        id = data.get('id')
        return id
