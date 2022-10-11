
from flask import Blueprint,request,json,jsonify
from pharm_service import PharmService
from flask import jsonify,Response
from flask_cors import CORS, cross_origin

pharms_resource = Blueprint('pharms_resource',__name__)
cors = CORS(pharms_resource)
pharmService = PharmService()


@pharms_resource.route('/api/pharms/<int:id>/',methods=['GET'])
def find(id):
    found = pharmService.find(id)
    if found is None:
        return Response(status=404)
    else:
        return jsonify(found)


@pharms_resource.route('/api/pharms/<int:id>/',methods=['DELETE'])
def delete(id):
    found = pharmService.find(id)
    if found is None:
        return Response(status=404)
    pharmService.delete(id)  
    return Response(status=204)

