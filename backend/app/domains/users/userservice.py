class UserService:
    def __init__(self):
        pass

    def get_users(self):
        return ["Alice", "Bob", "Charlie", "Delta"]


def get_user_service() -> UserService:
    return UserService()
