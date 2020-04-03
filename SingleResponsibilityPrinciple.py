"""
User class which is responsible for both the user properties and user database management

"""


class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass

    def save(self, user: 'User') -> 'User':
        pass


"""
Split User class into User and UserDB
"""


class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass
