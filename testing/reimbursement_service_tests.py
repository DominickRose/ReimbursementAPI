from entities.reimbursement import Reimbursement
from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres

from services.reimbursement_service import ReimbursementService
from services.reimbursement_service_impl import ReimbursementServiceImpl

from unittest.mock import MagicMock

reimbursement_dao: ReimbursementDao = ReimbursementDaoPostgres()

test_list = [
    Reimbursement(1, 1, 200, "Food", "Approved", "Sure"),
    Reimbursement(2, 1, 400, 'Gas',  'Pending', ''),
    Reimbursement(3, 2, 50, 'Please', 'Pending', ''),
    Reimbursement(4, 2, 600, 'Sup',  'Rejected', 'Please give a valid reason'),
    Reimbursement(5, 1, 1000, 'Im poor', 'Approved', 'K' )
]

reimbursement_dao.get_all_reimbursements = MagicMock(return_value = test_list)
reimbursement_service: ReimbursementService = ReimbursementServiceImpl(reimbursement_dao)

def test_1_1_get_all_employee_1():
    results = reimbursement_service.get_all_reimbursements_for_user(1)
    assert len(results) == 3

def test_1_2_get_all_employee_2():
    results = reimbursement_service.get_all_reimbursements_for_user(2)
    assert len(results) == 2

def test_2_1_get_all_approved():
    results = reimbursement_service.get_all_reimbursements_of_status('Approved')
    assert len(results) == 2

def test_2_1_get_all_pending():
    results = reimbursement_service.get_all_reimbursements_of_status('Pending')
    assert len(results) == 2

def test_2_1_get_all_rejected():
    results = reimbursement_service.get_all_reimbursements_of_status('Rejected')
    assert len(results) == 1

def test_3_1_get_all_approved_for_emp_1():
    results = reimbursement_service.get_all_reimbursements_of_status_for_user(1, 'Approved')
    assert len(results) == 2

def test_3_2_get_all_pending_for_emp_1():
    results = reimbursement_service.get_all_reimbursements_of_status_for_user(1, 'Pending')
    assert len(results) == 1
