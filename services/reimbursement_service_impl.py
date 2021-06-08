from typing import List

from entities.reimbursement import Reimbursement
from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres

from services.reimbursement_service import ReimbursementService

class ReimbursementServiceImpl(ReimbursementService):
    def __init__(self, reimbursement_dao: ReimbursementDao):
        self.reimbursement_dao = reimbursement_dao

    def add_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        return self.reimbursement_dao.add_reimbursement(reimbursement)

    def get_single_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        return self.reimbursement_dao.get_single_reimbursement(reimbursement_id)

    def get_all_reimbursements(self) -> List[Reimbursement]:
        return self.reimbursement_dao.get_all_reimbursements()

    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        return self.reimbursement_dao.update_reimbursement(reimbursement)

    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        return self.reimbursement_dao.delete_reimbursement(reimbursement_id)

    def get_all_reimbursements_for_user(self, user_id: int) -> List[Reimbursement]:
        all_reimbursements = self.reimbursement_dao.get_all_reimbursements()
        return [reimbursement for reimbursement in all_reimbursements if reimbursement.owner_id == user_id]

    def get_all_reimbursements_of_status(self, type: str) -> List[Reimbursement]:
        all_reimbursements = self.reimbursement_dao.get_all_reimbursements()
        return [reimbursement for reimbursement in all_reimbursements if reimbursement.status == type]

    def get_all_reimbursements_of_status_for_user(self, user_id, type: str) -> List[Reimbursement]:
        all_reimbursements = self.reimbursement_dao.get_all_reimbursements()
        return [reimbursement for reimbursement in all_reimbursements if reimbursement.status == type and reimbursement.owner_id == user_id]

