from flask import jsonify, request

from exceptions import NotFoundError, MissingDataError
from extensions import app
from mappers import UserMapper
from models import db, Post
from repos import UserRepos
from serializers import UserJsonSerializer, ErrorJsonSerializer
from services import UserService

user_repos = UserRepos()
user_mapper = UserMapper()
user_service = UserService(user_repos, user_mapper)
user_serializer = UserJsonSerializer()
error_serializer = ErrorJsonSerializer()


class UserController:

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
        posts = Post.query.all()
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

    @staticmethod
    @app.route('/posts', methods=['POST'])
    def create_post():
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        user_id = data.get('user_id')



        if not title or not content:
            return jsonify({"message": "Name and age are required"}), 400

        new_post = Post(title=title, content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'id': new_post.id, 'title': new_post.title, 'content': new_post.content}), 201
