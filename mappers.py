from numpy.core.defchararray import title

from dtos import UserGetDto, PostGetDto
from models import User, Post


class UserMapper:
    def users_to_user_gets(self, user_list):
        return [self.user_to_user_get(user) for user in user_list]

    def user_to_user_get(self, user):
        return UserGetDto(user.name, user.age, user.id)

    def user_create_to_user(self, user_create):
        return User(name = user_create.name, age =user_create.age)

class PostMapper:
    def posts_to_post_gets(self, post_list):
        return [self.post_to_post_get(post) for post in post_list]

    def post_to_post_get(self, post):
        return PostGetDto(title=post.title, content=post.content, id=post.id, user_id=post.user_id)

    def post_create_to_post(self, post_create):
        return Post(title=post_create.title, content=post_create.content, user_id=post_create.user_id)