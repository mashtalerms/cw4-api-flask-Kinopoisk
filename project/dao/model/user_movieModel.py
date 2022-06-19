from marshmallow import Schema, fields

from dao.model.movieModel import MovieSchema
from dao.model.userModel import UserSchema
from setup_db import db


class UserMovie(db.Model):
	__tablename__ = 'user_movie'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	favorite_movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)

	user = db.relationship('User')
	movie = db.relationship("Movie")


class UserMovieSchema(Schema):
	id = fields.Int()
	user_id = fields.Nested(UserSchema)
	favorite_movie_id = fields.Nested(MovieSchema)
