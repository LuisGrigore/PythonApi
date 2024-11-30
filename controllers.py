from flask import jsonify, request

from exceptions import NotFoundError, MissingDataError
from extensions import app
from mappers import UserMapper, PostMapper
from models import db, Post
from repos import UserRepos, PostRepos
from serializers import UserJsonSerializer, ErrorJsonSerializer, PostJsonSerializer
from services import UserService, PostService

user_repos = UserRepos()
user_mapper = UserMapper()
user_service = UserService(user_repos, user_mapper)
user_serializer = UserJsonSerializer()

error_serializer = ErrorJsonSerializer()

post_repos = PostRepos()
post_mapper = PostMapper()
post_service = PostService(post_repos,post_mapper)
post_serializer = PostJsonSerializer()


class UserController:

    @staticmethod
    @app.route('/users/<int:user_id>/posts', methods=['GET'])
    def get_user_posts(user_id):
        try:
            posts = post_service.get_by_user_id(user_id)
            return post_serializer.serialize_post_get_dtos(posts)
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e), 404

    @staticmethod
    @app.route('/users', methods=['GET'])
    def get_users():
        try:
            return user_serializer.serialize_user_get_dtos(user_service.get_all())
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e), 404

    @staticmethod
    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        try:
            user = user_service.get(user_id)
            return user_serializer.serialize_user_get_dto(user)
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e), 404

    @staticmethod
    @app.route('/users', methods=['POST'])
    def create_user():
        try:
            user_create_dto = user_serializer.deserialize_user_create_dto(request.get_json())
            return user_serializer.serialize_user_get_dto(user_service.create(user_create_dto)), 201
        except MissingDataError as e:
            return error_serializer.serialize_error_message(e), 400

    @staticmethod
    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        try:
            data = request.get_json()
            new_user = user_serializer.deserialize_user_create_dto(data)
            return user_serializer.serialize_user_get_dto(user_service.update(user_id, new_user))
        except MissingDataError as e:
            return error_serializer.serialize_error_message(e), 400
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e), 404

    @staticmethod
    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        try:
            return user_serializer.serialize_user_get_dto(user_service.delete(user_id))
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e), 404

class PostsController:

    @staticmethod
    @app.route('/posts', methods=['GET'])
    def get_posts():
        try:
            return post_serializer.serialize_post_get_dtos(post_service.get_all())
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e)

    @staticmethod
    @app.route('/posts/<int:post_id>', methods=['GET'])
    def get_post(post_id):
        try:
            post = post_service.get(post_id)
            return post_serializer.serialize_post_get_dto(post)
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e), 404

    @staticmethod
    @app.route('/posts', methods=['POST'])
    def create_post():
        try:
            data = request.get_json()
            return post_serializer.serialize_post_get_dto(post_service.create(post_serializer.deserialize_post_create_dto(data)))
        except MissingDataError as e:
            return error_serializer.serialize_error_message(e)

    @staticmethod
    @app.route('/posts/<int:post_id>', methods=['PUT'])
    def update_post(post_id):
        try:
            data = request.get_json()
            new_post = post_serializer.deserialize_post_create_dto(data)
            return post_serializer.serialize_post_get_dto(post_service.update(post_id, new_post))
        except MissingDataError as e:
            return error_serializer.serialize_error_message(e), 400
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e), 404

    @staticmethod
    @app.route('/posts/<int:post_id>', methods=['DELETE'])
    def delete_post(post_id):
        try:
            return post_serializer.serialize_post_get_dto(post_service.delete(post_id))
        except NotFoundError as e:
            return error_serializer.serialize_error_message(e), 404
