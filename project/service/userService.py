import base64
import hashlib
import hmac

from werkzeug.exceptions import MethodNotAllowed

from project.dao.userDao import UserDAO
from project.exceptions import ItemNotFound, IncorrectPassword, UserAlreadyExists
from flask import current_app


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_by_email(self, email):
        user = self.dao.get_by_email(email)
        if not user:
            raise ItemNotFound
        return user

    def create(self, data):
        user = self.dao.get_by_email(data.get('email'))
        if user:
            raise UserAlreadyExists

        data['password'] = self.generate_password(data.get('password'))
        return self.dao.create(data)

    def update(self, data, email):
        self.get_by_email(email)
        if 'password' not in data.keys() and 'email' not in data.keys():
            self.dao.update_by_email(data, email)

    def compare_passwords(self, password_hash, other_password):
        decoded_digest = base64.b64decode(password_hash)
        hash_digest = self.create_hash(other_password)

        return hmac.compare_digest(decoded_digest, hash_digest)

    def update_password(self, data, email):
        user = self.get_by_email(email)
        current_password = data.get('old_password')
        new_password = data.get('new_password')

        if None in [current_password, new_password]:
            raise MethodNotAllowed

        if not self.compare_passwords(user.password, current_password):
            raise IncorrectPassword

        data = {
            'password': self.generate_password(new_password)
        }
        self.dao.update_by_email(data, email)

    def create_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            current_app.config.get("PWD_HASH_SALT"),
            current_app.config.get("PWD_HASH_ITERATIONS")
        )
        return hash_digest

    def generate_password(self, password):
        hash_digest = self.create_hash(password)
        b_encode = base64.b64encode(hash_digest)
        return b_encode
