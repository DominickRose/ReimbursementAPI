from entities.user import User
from daos.user_dao import UserDao
from daos.user_dao_postgres import UserDaoPostgres
from exceptions.exceptions import ResourceNotFoundError

import uuid

user_dao: UserDao = UserDaoPostgres()

username = str(uuid.uuid4())[:20]
testUser1 = User(0, username, 'x', 'Test', 'User', 'emp')

username2 = str(uuid.uuid4())[:20]
testUser2 = User(0, username2, 'x', 'Test', 'User', 'emp')

def test_1_1_add_user():
    result = user_dao.add_user(testUser1)
    assert result.user_id == testUser1.user_id

def test_1_2_add_user():
    result = user_dao.add_user(testUser2)
    assert result.user_id != 0

def test_1_3_add_duplicate_username():
    try:
        user_dao.add_user(testUser2)
        assert False
    except ValueError as e:
        assert str(e) == "A user with that username already exists"

def test_2_1_get_all_users():
    result = user_dao.get_all_users()
    assert len(result) >= 2

def test_3_1_get_single_user():
    result = user_dao.get_single_user(testUser1.user_id)
    assert result.user_id == testUser1.user_id

def test_3_2_get_invalid_user():
    try:
        user_dao.delete_user(0)
        assert False
    except ResourceNotFoundError as e:
        assert str(e) == "Resource with given ID 0 not found"

def test_4_1_update_user():
    testUser1.first_name = "John"
    result = user_dao.update_user(testUser1)
    assert result.first_name == 'John'

def test_4_2_update_nonexistent_user():
    invalid_user = User(0, '', '', '', '', '')
    try:
        user_dao.update_user(invalid_user)
        assert False
    except ResourceNotFoundError as e:
        assert str(e) == "Resource with given ID 0 not found"

def test_5_1_delete_user():
    result1 = user_dao.delete_user(testUser1.user_id)
    result2 = user_dao.delete_user(testUser2.user_id)
    assert result1
    assert result2

def test_5_2_delete_invalid_user():
    try:
        user_dao.delete_user(testUser1.user_id)
        assert False
    except ResourceNotFoundError as e:
        assert str(e) == f"Resource with given ID {testUser1.user_id} not found"