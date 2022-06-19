from dao.directorDao import DirectorDAO
from dao.genreDao import GenreDAO
from dao.movieDao import MovieDAO
from dao.userDao import UserDAO
from dao.user_movieDao import UserMovieDAO
from service.authService import AuthService
from service.directorService import DirectorService
from service.genreService import GenreService
from service.movieService import MovieService
from service.userService import UserService
from service.user_movieService import UserMovieService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
user_movie_dao = UserMovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)
user_movie_service = UserMovieService(dao=user_movie_dao)
