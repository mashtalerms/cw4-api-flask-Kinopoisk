from sqlalchemy.exc import IntegrityError

from project.BaseConfig import DevelopmentConfig
from project.dao.model.directorModel import Director
from project.dao.model.genreModel import Genre
from project.dao.model.movieModel import Movie
from project.dao.model.userModel import User
from project.server import create_app
from project.setup_db import db
from project.utils import read_json

app = create_app(DevelopmentConfig)

data = read_json("fixtures.json")

with app.app_context():
    for genre in data["genres"]:
        db.session.add(Genre(**genre))

    for movie in data["movies"]:
        db.session.add(Movie(**movie))

    for director in data["directors"]:
        db.session.add(Director(**director))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
