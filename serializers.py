from flask import jsonify

from dtos import UserCreateDto, PostCreateDto
from error_messages import CREATE_USER_MISSING_DATA
from exceptions import MissingDataError


class UserJsonSerializer:
    def serialize_user_get_dtos(self,user_get_dtos):
        return jsonify([{'id': user.user_id, 'name': user.name, 'age': user.age} for user in user_get_dtos])

    def serialize_user_get_dto(self,user_get_dto):
        return jsonify({'id': user_get_dto.user_id, 'name': user_get_dto.name, 'age': user_get_dto.age})

    def deserialize_user_create_dto(self,data):
        name = data.get('name')
        age = data.get('age')
        if not name or not age:
            raise MissingDataError(CREATE_USER_MISSING_DATA)
        return UserCreateDto(name, age)

class PostJsonSerializer:
    def serialize_post_get_dtos(self,post_get_dtos):
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id} for post in post_get_dtos])

    def serialize_post_get_dto(self,post_get_dto):
        return jsonify({'id': post_get_dto.id, 'title': post_get_dto.title, 'content': post_get_dto.content, 'user_id': post_get_dto.user_id})

    def deserialize_post_create_dto(self,data):
        title = data.get('title')
        content = data.get('content')
        user_id = data.get('user_id')
        if not title or not content or not user_id:
            raise MissingDataError(CREATE_POST_MISSING_DATA)
        return PostCreateDto(title=title, content=content,user_id=user_id)


class ErrorJsonSerializer:
    def serialize_error_message(self,error):
        return jsonify({'message': error.message})
