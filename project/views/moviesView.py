from flask import request
from flask_restx import Resource, Namespace

from project.dao.model.movieModel import MovieSchema
from project.implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        page = request.args.get("page")
        status = request.args.get("status")

        all_movies = movie_service.get_all(page, status)
        res = movies_schema.dump(all_movies)
        return res, 200


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200
