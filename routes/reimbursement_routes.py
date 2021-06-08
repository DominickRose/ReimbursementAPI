from flask import Flask, request, jsonify

from entities.reimbursement import Reimbursement
from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres

from services.reimbursement_service_impl import ReimbursementServiceImpl

from exceptions.exceptions import ResourceNotFoundError

reimbursement_dao: ReimbursementDao = ReimbursementDaoPostgres()
reimbursement_service = ReimbursementServiceImpl(reimbursement_dao)


def reimbursement_routes(app: Flask):
    @app.post('/reimbursements')
    def add_reimbursement():
        new_reimbursement = Reimbursement.from_json(request.json)
        reimbursement_service.add_reimbursement(new_reimbursement)
        return jsonify(new_reimbursement.json()), 201

    @app.get('/reimbursements')
    def get_all_reimbursements():
        owner = request.args.get('owner')
        status = request.args.get('status')
        all_reimbursements = []
        if owner == None and status == None:
            all_reimbursements = reimbursement_service.get_all_reimbursements()
        elif owner == None or not owner.isnumeric():
            all_reimbursements = reimbursement_service.get_all_reimbursements_of_status(status)
        elif status == None:
            all_reimbursements = reimbursement_service.get_all_reimbursements_for_user(int(owner))
        else:
            all_reimbursements = reimbursement_service.get_all_reimbursements_of_status_for_user(int(owner), status)
        return jsonify([reimbursement.json() for reimbursement in all_reimbursements]), 200

    @app.get('/reimbursements/<reimbursement_id>')
    def get_single_reimbursement(reimbursement_id: str):
        if not reimbursement_id.isnumeric():
            return "Invalid URI, reimbursement ID must be numeric"
        try:
            reimbursement = reimbursement_service.get_single_reimbursement(int(reimbursement_id))
            return jsonify(reimbursement.json()), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.put('/reimbursements/<reimbursement_id>')
    def update_reimbursement(reimbursement_id: str):
        if not reimbursement_id.isnumeric():
            return "Invalid URI, reimbursement ID must be numeric"
        try:
            to_update = Reimbursement.from_json(request.json)
            to_update.reimbursement_id = int(reimbursement_id)
            updated = reimbursement_service.update_reimbursement(to_update)
            return jsonify(updated.json()), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.delete('/reimbursements/<reimbursement_id>')
    def delete_reimbursement(reimbursement_id: str):
        if not reimbursement_id.isnumeric():
            return "Invalid URI, reimbursement ID must be numeric"
        try:
            reimbursement_service.delete_reimbursement(int(reimbursement_id))
            return f"Successfully deleted reimbursement with id {reimbursement_id}", 205
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.patch('/reimbursements/<reimbursement_id>/approve_or_deny')
    def approve_or_deny(reimbursement_id: str):
        if not reimbursement_id.isnumeric():
            return "Reimbursement ID must be numeric", 400
        if 'status' in request.json and 'mgr_message' in request.json:
            try:
                reimbursement = reimbursement_service.get_single_reimbursement(int(reimbursement_id))
                reimbursement.status = request.json['status']
                reimbursement.mgr_message = request.json['mgr_message']
                updated = reimbursement_service.update_reimbursement(reimbursement)
                return jsonify(updated.json()), 200
            except ResourceNotFoundError as e:
                return str(e), 404
        else:
            return "Invalid JSON body", 400