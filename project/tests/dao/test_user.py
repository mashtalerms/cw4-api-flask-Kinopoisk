import pytest

from project.dao.model.userModel import User
from project.dao.userDao import UserDAO


class TestUserDAO:
    @pytest.fixture(autouse=True)
    def dao(self, db):
        self.dao = UserDAO(db.session)

    def test_create(self):
        data = {
            "email": "test",
            "password": "test",
            "name": "test"
        }
        user = self.dao.create(data)

        assert user is not None
        assert user.id is not None

    def test_update_by_email(self):
        user_d = {
            "email": "TEST",
            "password": "TEST"
        }
        user = self.dao.create(user_d)
        email = "Test update"

        self.dao.update_by_email(email, user_d)

    def test_get_by_email(self):
        user_d = {
            "email": "TEST",
            "password": "TEST"
        }
        user = self.dao.create(user_d)

        email_1 = "TEST"
        email_2 = "NNN"

        assert self.dao.get_by_email(email_1) is not None
        assert self.dao.get_by_email(email_2) is None


    #
    # @pytest.fixture
    # def user_2(self, db):
    #     user = {
    #         "email": "test2",
    #         "password": "test2",
    #         "name": "test2",
    #         "surname": "test2",
    #         "favourite_genre": "2",
    #     }
    #     g = User(**user)
    #     db.session.add(g)
    #     db.session.commit()
    #     return g

    # def test_get_user_by_id(self, movie_1):
    #     assert self.dao.get_one(movie_1.id) == movie_1
    #
    # def test_get_movie_by_id_not_found(self):
    #     assert self.dao.get_one(1) is None
    #
    # def test_get_all_movies(self, movie_1, movie_2):
    #     assert self.dao.get_all(page=None, status=None) == [movie_1, movie_2]
