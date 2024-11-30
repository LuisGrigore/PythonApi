from abc import ABC, abstractmethod

from error_messages import NO_USERS_FOUND, USER_NOT_FOUND, NO_POSTS_FOUND, POST_NOT_FOUND
from exceptions import NotFoundError

class CrudService(ABC):
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


class UserService(CrudService):
    def __init__(self, user_repos, user_mapper):
        self.user_repos = user_repos
        self.user_mapper = user_mapper

    def get_all(self):
        users = self.user_repos.get_all()
        if not users:
            raise NotFoundError(NO_USERS_FOUND)
        return self.user_mapper.users_to_user_gets(users)

    def get(self, user_id):
        user = self.user_repos.get(user_id)
        if user is None:
            raise NotFoundError(USER_NOT_FOUND)
        return self.user_mapper.user_to_user_get(user)

    def create(self, create_user_dto):
        user = self.user_mapper.user_create_to_user(create_user_dto)
        return self.user_mapper.user_to_user_get(self.user_repos.create(user))

    def delete(self, user_id):
        user = self.user_repos.get(user_id)
        if user:
            return self.user_mapper.user_to_user_get(self.user_repos.delete(user))
        raise NotFoundError(USER_NOT_FOUND)

    def update(self, user_id, new_user):
        user = self.user_repos.get(user_id)
        if user:
            return self.user_mapper.user_to_user_get(self.user_repos.update(user_id, new_user))
        else:
            raise NotFoundError(USER_NOT_FOUND)



class PostService(CrudService):
    def __init__(self, post_repos, post_mapper):
        self.post_repos = post_repos
        self.post_mapper = post_mapper

    def get_all(self):
        users = self.post_repos.get_all()
        if not users:
            raise NotFoundError(NO_POSTS_FOUND)
        return self.post_mapper.users_to_user_gets(users)

    def get(self, post_id):
        user = self.post_repos.get(post_id)
        if user is None:
            raise NotFoundError(POST_NOT_FOUND)
        return self.post_mapper.user_to_user_get(user)

    def create(self, create_post_dto):
        user = self.post_mapper.user_create_to_user(create_post_dto)
        return self.post_mapper.user_to_user_get(self.post_repos.create(user))

    def delete(self, post_id):
        user = self.post_repos.get(post_id)
        if user:
            return self.post_mapper.user_to_user_get(self.post_repos.delete(user))
        raise NotFoundError(POST_NOT_FOUND)

    def update(self, post_id, new_post):
        user = self.post_repos.get(post_id)
        if user:
            return self.post_mapper.user_to_user_get(self.post_repos.update(post_id, new_post))
        else:
            raise NotFoundError(POST_NOT_FOUND)