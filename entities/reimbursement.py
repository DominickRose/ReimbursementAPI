class Reimbursement:
    def __init__(self, reimbursement_id: int, owner_id: int, amount: int, reason: str, status: str, mgr_message: str):
        self.reimbursement_id = reimbursement_id
        self.owner_id = owner_id
        self.amount = amount
        self.reason = reason
        self.status = status
        self.mgr_message = mgr_message

    def json(self):
        return {
            'reimbursementId': self.reimbursement_id,
            'ownerId': self.owner_id,
            'amount': self.amount,
            'reason': self.reason,
            'status': self.status,
            'mgrMessage' : self.mgr_message
        }

    @staticmethod
    def from_json(json):
        reimbursement = Reimbursement(0, 0, 0, '', '', '')
        reimbursement.reimbursement_id = json['reimbursementId']
        reimbursement.owner_id = json['ownerId']
        reimbursement.amount = json['amount']
        reimbursement.reason = json['reason']
        reimbursement.status = json['status']
        reimbursement.mgr_message = json['mgrMessage']
        return reimbursement