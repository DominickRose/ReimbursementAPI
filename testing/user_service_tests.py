from entities.user import User
from daos.user_dao import UserDao
from daos.user_dao_postgres import UserDaoPostgres

from services.user_service import UserService
from services.user_service_impl import UserServiceImpl

from exceptions.exceptions import InvalidCredentialsError

from unittest.mock import MagicMock

user_dao: UserDao = UserDaoPostgres()

user = User(1, "Test", "Test123", "Test", "Cart", "Emp")
user2 = User(2, "Hello", "There", "Test", "2", "MGR")
user_dao.get_all_users = MagicMock(return_value = [user, user2])

user_service: UserService = UserServiceImpl(user_dao)

def test_1_1_login_valid():
    result = user_service.login("Test", "Test123")
    assert result[0] == "Emp"
    assert result[1] == 1

def test_1_2_login_valid():
    result = user_service.login("Hello", "There")
    assert result[0] == "MGR"
    assert result[1] == 2

def test_1_3_invalid_username():
    try:
        user_service.login("Temp", "Test123")
        assert False
    except InvalidCredentialsError as e:
        assert str(e) == "Invalid login credentials"

def test_1_4_invalid_password():
    try:
        user_service.login("Test", "X")
        assert False
    except InvalidCredentialsError as e:
        assert str(e) == "Invalid login credentials"