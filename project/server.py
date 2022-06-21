from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api
from flask_swagger_ui import get_swaggerui_blueprint

from project.setup_db import db
from project.views.authView import auth_ns
from project.views.directorsView import director_ns
from project.views.genresView import genre_ns
from project.views.moviesView import movie_ns
from project.views.userView import user_ns

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 3",
    doc="/docs",
)

# Нужно для работы с фронтендом
cors = CORS()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template('index.html')

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)

    # #Swagger
    # SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    # API_URL = 'http://217.0.0.1:25000/swagger'  # Our API url (can of course be a local resource)
    #
    # # Call factory function to create our blueprint
    # swaggerui_blueprint = get_swaggerui_blueprint(
    #     SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    #     API_URL,
    #     config={  # Swagger UI config overrides
    #         'app_name': "Test application"
    #     },
    # )
    #
    # app.register_blueprint(swaggerui_blueprint)

    return app
