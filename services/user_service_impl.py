from typing import List, Tuple

from entities.user import User
from daos.user_dao import UserDao
from services.user_service import UserService

from exceptions.exceptions import InvalidCredentialsError

class UserServiceImpl(UserService):
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao


    def add_user(self, user: User) -> User:
        return self.user_dao.add_user(user)


    def get_single_user(self, user_id: int) -> User:
        return self.user_dao.get_single_user(user_id)


    def get_all_users(self) -> List[User]:
        return self.user_dao.get_all_users()


    def update_user(self, user: User) -> User:
        return self.user_dao.update_user(user)


    def delete_user(self, user_id: int) -> bool:
        return self.user_dao.delete_user(user_id)


    def login(self, username: str, password: str) -> Tuple[str, int]:
        users = self.user_dao.get_all_users()
        user = [user for user in users if user.username == username]
        if len(user) == 0:
            raise InvalidCredentialsError("Invalid login credentials")
        elif user[0].password != password:
            raise InvalidCredentialsError("Invalid login credentials")
        else:
            return (user[0].emp_or_mgr, user[0].user_id)
