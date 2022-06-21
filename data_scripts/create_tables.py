import os, sys
path = os.path.abspath('.')
sys.path.insert(1, path)

from project.BaseConfig import DevelopmentConfig
from project.dao.model import movieModel, genreModel, directorModel, userModel
from project.server import create_app
from project.setup_db import db

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
