# import pytest
#
# from project.dao.model.movieModel import Movie
# from project.dao.movieDao import MovieDAO
#
#
# class TestMovieDAO:
#     @pytest.fixture(autouse=True)
#     def dao(self, db):
#         self.dao = MovieDAO(db.session)
#
#     @pytest.fixture
#     def movie_1(self, db):
#         movie = {
#             "title": "test",
#             "description": "test",
#             "trailer": "test",
#             "year": "1",
#             "rating": "1",
#             "genre_id": "1",
#             "director_id": "1"
#         }
#         g = Movie(**movie)
#         db.session.add(g)
#         db.session.commit()
#         return g
#
#     @pytest.fixture
#     def movie_2(self, db):
#         movie = {
#             "title": "test_2",
#             "description": "test_2",
#             "trailer": "test_2",
#             "year": "2",
#             "rating": "2",
#             "genre_id": "2",
#             "director_id": "2"
#         }
#         g = Movie(**movie)
#         db.session.add(g)
#         db.session.commit()
#         return g
#
#     def test_get_movie_by_id(self, movie_1):
#         assert self.dao.get_one(movie_1.id) == movie_1
#
#     def test_get_movie_by_id_not_found(self):
#         assert self.dao.get_one(1) is None
#
#     def test_get_all_movies(self, movie_1, movie_2):
#         assert self.dao.get_all(page=None, status=None) == [movie_1, movie_2]
