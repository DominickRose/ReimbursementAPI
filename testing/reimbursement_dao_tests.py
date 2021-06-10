from entities.reimbursement import Reimbursement
from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres

from entities.user import User
from daos.user_dao import UserDao
from daos.user_dao_postgres import UserDaoPostgres

from exceptions.exceptions import ResourceNotFoundError

import uuid


user_dao : UserDao = UserDaoPostgres()
reimbursement_dao: ReimbursementDao = ReimbursementDaoPostgres()

username = str(uuid.uuid4())[:20]
test_user = User(0, username, 'x', 'Test', 'Owner', "emp")
user_dao.add_user(test_user)

test_reimbursement = Reimbursement(0, test_user.user_id, 100, '', 'Pending', '', 0)
test_reimbursement_2 = Reimbursement(0, test_user.user_id, 200, '', 'Pending', '', 0)


def test_1_1_add_reimbursement():
    result = reimbursement_dao.add_reimbursement(test_reimbursement)
    assert result.reimbursement_id == test_reimbursement.reimbursement_id

def test_1_2_add_reimbursement():
    result = reimbursement_dao.add_reimbursement(test_reimbursement_2)
    assert result.reimbursement_id != 0

def test_2_1_get_single_reimbursement():
    result = reimbursement_dao.get_single_reimbursement(test_reimbursement.reimbursement_id)
    assert result.reimbursement_id == test_reimbursement.reimbursement_id

def test_2_2_get_invalid_reimbursement():
    try:
       reimbursement_dao.get_single_reimbursement(0)
       assert False
    except ResourceNotFoundError as e:
        assert str(e) == "Resource with given ID 0 not found"

def test_3_1_get_all_reimbursements():
    results = reimbursement_dao.get_all_reimbursements()
    assert len(results) >= 2

def test_4_1_update_account():
    test_reimbursement.amount = 500
    result = reimbursement_dao.update_reimbursement(test_reimbursement)
    assert result.amount == 500

def test_4_2_update_invalid_account():
    invalid = Reimbursement(0, test_user.user_id, 0, '', '', '', 0)
    try:
        reimbursement_dao.update_reimbursement(invalid)
        assert False
    except ResourceNotFoundError as e:
        assert str(e) == "Resource with given ID 0 not found"

def test_5_1_delete_account():
    assert reimbursement_dao.delete_reimbursement(test_reimbursement.reimbursement_id)

def test_5_2_delete_invalid_account():
    try:
        reimbursement_dao.delete_reimbursement(0)
        assert False
    except ResourceNotFoundError as e:
        assert str(e) == "Resource with given ID 0 not found"
