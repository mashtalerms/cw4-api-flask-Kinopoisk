from project.dao.user_movieDao import UserMovieDAO


class UserMovieService:
    def __init__(self, dao: UserMovieDAO):
        self.dao = dao

    def add_favorite_movie(self, user_id, movie):
        data = {
            "user_id": user_id,
            "movie_id": movie.id
        }
        return self.dao.add_favorite_movie(data)

    def delete(self, user, movie):
        pass


