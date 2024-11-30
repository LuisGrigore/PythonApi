from flask import jsonify

from dtos import UserCreateDto
from error_messages import NAME_AGE_REQUIRED
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
            raise MissingDataError(NAME_AGE_REQUIRED)
        return UserCreateDto(name, age)

class ErrorJsonSerializer:
    def serialize_error_message(self,error):
        return jsonify({'message': error.message})
