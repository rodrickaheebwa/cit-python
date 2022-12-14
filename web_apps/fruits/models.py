import hashlib
from fruits import db
from datetime import datetime
from flask_login import UserMixin

class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Fruit(db.Model, ExtraMixin):
    __tablename__ = 'fruits'
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

class HackerNews(db.Model, ExtraMixin):
    __tablename__ = 'hacker_news'
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'created_at': str(self.created_at),
        }

    @classmethod
    def get_all_news(cls):
        return cls.query.all()

class CbsNews(db.Model, ExtraMixin):
    __tablename__ = 'cbs_news'
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)

    @classmethod
    def get_all_news(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'description' : self.description,
            'image': self.image
        }


class User(UserMixin, db.Model, ExtraMixin):
    __tablename__ = 'users'
    username = db.Column(db.String(100), nullable=False, unique = True)
    email = db.Column(db.String(100), nullable=False, unique = True)
    password = db.Column(db.String(100), nullable=False)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, hashed_password):
        return User.hash_password(password) == hashed_password

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_user_by_username(cls, username):
        # select * from users where username = username
        return cls.query.filter_by(username=username).first()

class Todo(db.Model, ExtraMixin):
    __tablename__ = 'todos'
    todo = db.Column(db.String(100), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def delete_instance(self, using_transaction=True, keep_parents=False):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_todos(cls):
        return cls.query.all()

    @classmethod
    def get_todos_by_user_id(cls, user_id):
        return cls.query.filter_by(created_by=user_id).all()

    @classmethod
    def get_by_id(cls, todo_id):
        return cls.query.filter_by(id=todo_id).first()