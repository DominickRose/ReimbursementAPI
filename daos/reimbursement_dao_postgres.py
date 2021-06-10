from typing import List

from entities.reimbursement import Reimbursement
from daos.reimbursement_dao import ReimbursementDao

from exceptions.exceptions import ResourceNotFoundError

from utils.connection_util import connection

class ReimbursementDaoPostgres(ReimbursementDao):
    def add_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = """insert into reimbursement (owner_id, amount, reason, status, mgr_message, submit_date) values (%s, %s, %s, %s, %s, %s) returning reimbursement_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.owner_id, reimbursement.amount, reimbursement.reason, reimbursement.status, reimbursement.mgr_message, reimbursement.date))
        connection.commit()
        reimbursement_id = cursor.fetchone()[0]
        reimbursement.reimbursement_id = reimbursement_id
        return reimbursement

    def get_single_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        sql = """select * from reimbursement where reimbursement_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        record = cursor.fetchone()
        try:
            return Reimbursement(*record)
        except TypeError:
            raise ResourceNotFoundError(f'Resource with given ID {reimbursement_id} not found')

    def get_all_reimbursements(self) -> List[Reimbursement]:
        sql = """select * from reimbursement"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        return [Reimbursement(*record) for record in records]

    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        self.get_single_reimbursement(reimbursement.reimbursement_id)

        sql = """update reimbursement set owner_id = %s, amount=%s, reason=%s, status=%s, mgr_message=%s, submit_date=%s where reimbursement_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.owner_id, reimbursement.amount, reimbursement.reason, reimbursement.status, reimbursement.mgr_message, reimbursement.date, reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        self.get_single_reimbursement(reimbursement_id)

        sql = """delete from reimbursement where reimbursement_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        connection.commit()
        return True