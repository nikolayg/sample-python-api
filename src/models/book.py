from flask_restplus import fields
from server.instance import server

book = server.api.model('Book', {
    'id': fields.Integer(readOnly=True, description='Id'),
    'title': fields.String(required=True, description='Book title')
})