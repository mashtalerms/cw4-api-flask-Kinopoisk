from flask_restx import Resource, Namespace

from project.dao.model.directorModel import DirectorSchema
from project.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
@director_ns.doc()
class DirectorsView(Resource):
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:did>/')
@director_ns.doc(params={'did': 'Director ID'})
class DirectorView(Resource):
    def get(self, did):
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
