class UserCreateDto:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserGetDto:
    def __init__(self, name, age, user_id):
        self.name = name
        self.age = age
        self.user_id = user_id