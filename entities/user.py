class User:
    def __init__(self, user_id: id, username: str, password: str, first_name: str, last_name: str, emp_or_mgr: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.emp_or_mgr = emp_or_mgr

    def json(self):
        return {
            'userId': self.user_id,
            'username': self.username,
            'password': self.password,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'empOrMgr': self.emp_or_mgr
        }

    @staticmethod
    def from_json(json):
        user = User(0, '','','','','')
        user.user_id = json['userId']
        user.username = json['username']
        user.password = json['password']
        user.first_name = json['firstName']
        user.last_name = json['lastName']
        user.emp_or_mgr = json['empOrMgr']