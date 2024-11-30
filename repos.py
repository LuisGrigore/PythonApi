from abc import ABC, abstractmethod

from extensions import db
from models import User, Post


class CrudRepos(ABC):
    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def get(self, id):
        pass
    @abstractmethod
    def delete(self, id):
        pass
    @abstractmethod
    def create(self, create_dto):
        pass
    @abstractmethod
    def update(self, id, new_instance):
        pass

class UserRepos(CrudRepos):
    def __init__(self):
        pass
    def get_all(self):
        return User.query.all()

    def get(self,id):
        return User.query.get(id)

    def create(self,user):
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
        return user
    def update(self, user_id, new_user):
        user = self.get(user_id)
        user.name = new_user.name
        user.age = new_user.age
        db.session.commit()
        return user

class PostRepos(CrudRepos):
    def __init__(self):
        pass
    def get_all(self):
        return Post.query.all()

    def get(self,id):
        return Post.query.get(id)

    def create(self,post):
        db.session.add(post)
        db.session.commit()
        return post

    def delete(self, post):
        db.session.delete(post)
        db.session.commit()
        return post
    def update(self, post_id, new_post):
        post = self.get(post_id)
        post.title = new_post.title
        post.content = new_post.content
        db.session.commit()
        return post

    def get_by_user_id(self, user_id):
        return Post.query.filter_by(user_id=user_id).all()