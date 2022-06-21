from flask import current_app
from project.dao.model.movieModel import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, page, status):
        movies = self.session.query(Movie)

        if status == "new" and page is not None:
            page_int = int(page)
            movies_fresh = movies.order_by(Movie.year.desc())
            movies_fresh_and_paged = movies_fresh.paginate(page_int, current_app.config.ITEMS_PER_PAGE, False)
            return movies_fresh_and_paged.items

        if status == "new":
            return movies.order_by(Movie.year.desc())

        if page is not None:
            page_int = int(page)
            movies = movies.paginate(page_int, current_app.config.ITEMS_PER_PAGE, False)
            return movies.items

        else:
            return movies.all()
