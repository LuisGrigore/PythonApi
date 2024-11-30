
from dtos import UserGetDto, UserCreateDto
from models import User


class UserMapper:
    def users_to_user_gets(self, user_list):
        return [self.user_to_user_get(user) for user in user_list]

    def user_to_user_get(self, user):
        return UserGetDto(user.name, user.age, user.id)

    def user_create_to_user(self, user_create):
        return User(name = user_create.name, age =user_create.age)