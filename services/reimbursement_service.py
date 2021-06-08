from typing import List

from entities.reimbursement import Reimbursement

from abc import ABC, abstractmethod

class ReimbursementService(ABC):
    @abstractmethod
    def add_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def get_single_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        pass

    @abstractmethod
    def get_all_reimbursements(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_reimbursements_for_user(self, user_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_reimbursements_of_status(self, type: str) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_reimbursements_of_status_for_user(self, user_id, type: str) -> List[Reimbursement]:
        pass