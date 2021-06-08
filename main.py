from flask import Flask

from routes.user_routes import user_routes
from routes.reimbursement_routes import reimbursement_routes

import logging

app = Flask(__name__)
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%s(asctime)s %(levelname)s %(message)s')

user_routes(app)
reimbursement_routes(app)

if __name__ == '__main__':
    app.run()