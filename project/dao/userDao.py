from project.dao.model.userModel import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        ent = User(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update_by_email(self, data, email):
        self.session.query(User).filter(User.email == email).update(data)
        self.session.commit()

    def get_by_email(self, email):
        try:
            user = self.session.query(User).filter(User.email == email).first()
            return user
        except Exception:
            return None
