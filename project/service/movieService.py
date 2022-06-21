from project.dao.movieDao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, page, status):
        movies = self.dao.get_all(page, status)
        return movies
