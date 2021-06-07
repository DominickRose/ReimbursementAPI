from entities.reimbursement import Reimbursement
from abc import ABC, abstractmethod

from typing import List

class ReimbursementDao(ABC):
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