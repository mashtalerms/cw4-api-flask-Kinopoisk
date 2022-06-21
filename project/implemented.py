from project.dao.directorDao import DirectorDAO
from project.dao.genreDao import GenreDAO
from project.dao.movieDao import MovieDAO

from project.dao.userDao import UserDAO
from project.dao.user_movieDao import UserMovieDAO


from project.service.directorService import DirectorService
from project.service.genreService import GenreService
from project.service.movieService import MovieService

from project.service.userService import UserService
from project.service.user_movieService import UserMovieService
from project.service.authService import AuthService

from project.setup_db import db


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
