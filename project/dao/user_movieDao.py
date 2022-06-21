from project.dao.model.user_movieModel import UserMovie


class UserMovieDAO:
    def __init__(self, session):
        self.session = session

    def add_favorite_movie(self, data):
        ent = UserMovie(**data)
        self.session.add(ent)
        self.session.commit()

    def delete(self):
        pass