from flask import Blueprint, current_app, request
from sqlalchemy.orm.exc import UnmappedInstanceError, NoResultFound

api_addrbook = Blueprint('api_addrbook', __name__)


@api_addrbook.errorhandler(UnmappedInstanceError)
@api_addrbook.errorhandler(NoResultFound)
def handle_notfound(_):
    return 'data not found', 404


@api_addrbook.route('', methods = ['GET'])
def list_all():
    model = current_app.config['model']
    return {'addrbooks': model.list_all()}


@api_addrbook.route('/<int:addrbook_id>', methods = ['GET'])
def get(addrbook_id):
    model = current_app.config['model']
    return {'addrbook': model.get(addrbook_id)}


@api_addrbook.route('', methods = ['PUT'])
def add():
    model = current_app.config['model']
    data = request.get_json()
    if data is None:
        return 'bad format', 400
    addrbook_id = model.add(data.get('name'), data['email'],
                            data['phone'], data['address'])
    return {'addrbook': model.get(addrbook_id)}


@api_addrbook.route('/<int:addrbook_id>', methods = ['POST'])
def modify(addrbook_id):
    model = current_app.config['model']
    data = request.get_json()
    if data is None:
        return 'bad format', 400
    model.modify(addrbook_id,
                 data.get('name'), data.get('email'),
                 data.get('phone'), data.get('address'))
    return {'addrbook': model.get(addrbook_id)}


@api_addrbook.route('/<int:addrbook_id>', methods = ['DELETE'])
def delete(addrbook_id):
    model = current_app.config['model']
    model.delete(addrbook_id)
    return {'delete': 'done'}
