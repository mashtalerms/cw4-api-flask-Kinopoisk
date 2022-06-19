import pytest

from project.dao.model.directorModel import Director
from project.dao.directorDao import DirectorDAO


class TestDirectorDAO:
    @pytest.fixture(autouse=True)
    def dao(self, db):
        self.dao = DirectorDAO(db.session)

    @pytest.fixture
    def director_1(self, db):
        g = Director(name="Тейлор Шеридан")
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def director_2(self, db):
        g = Director(name="Квентин Тарантино")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_director_by_id(self, director_1):
        assert self.dao.get_one(director_1.id) == director_1

    def test_get_director_by_id_not_found(self):
        assert self.dao.get_one(1) is None

    def test_get_all_directors(self, director_1, director_2):
        assert self.dao.get_all() == [director_1, director_2]
