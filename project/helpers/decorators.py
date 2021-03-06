import jwt
from flask import request, abort, current_app


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(
                token,
                current_app.config.get('JWT_SECRET'),
                algorithms=[current_app.config.get('JWT_ALGORITHM') ])
        except Exception as e:
            print(f"Traceback: {e}")
            abort(401)
        return func(*args, **kwargs)
    return wrapper


# def admin_required(func):
#     def wrapper(*args, **kwargs):
#         if 'Authorization' not in request.headers:
#             abort(401)
#
#         data = request.headers['Authorization']
#         token = data.split("Bearer ")[-1]
#         try:
#             user = jwt.decode(token, secret, algorithms=[algo])
#             role = user.get("role")
#         except Exception as e:
#             print("JWT Decode Exception", e)
#             abort(401)
#         if role != "admin":
#             abort(403)
#         return func(*args, **kwargs)
#     return
