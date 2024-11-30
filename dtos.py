class UserCreateDto:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserGetDto:
    def __init__(self, name, age, user_id):
        self.name = name
        self.age = age
        self.user_id = user_id

class PostCreateDto:
    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

class PostGetDto:
    def __init__(self, title, content, id, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.id = id