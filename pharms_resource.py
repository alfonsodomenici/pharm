
from flask import Blueprint,request,json,jsonify
from pharm_service import PharmService
from box_service import BoxService
from flask import jsonify,Response
from flask_cors import CORS, cross_origin
from util import json_serial

pharms_resource = Blueprint('pharms_resource',__name__)
cors = CORS(pharms_resource)
pharmService = PharmService()
boxService = BoxService()

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

@pharms_resource.route('/api/pharms/<int:id>/boxes',methods=['POST'])
def createBox(id):
    found = pharmService.find(id)
    if found is None:
        return Response(status=404)
    number = request.json['number']
    color = request.json['color']
    message = request.json['message']
    timebox = request.json['timebox']
    deltatime = request.json['deltatime']
    #status = request.json['status']
    created = boxService.create(id,number,color,message,timebox,deltatime)
    print(created)
    return Response(response=json.dumps(created, default=json_serial),
        status=201,
        mimetype='application/json')

@pharms_resource.route('/api/pharms/<int:id>/boxes',methods=['GET'])
def boxes(id):
    data = boxService.boxesByPharm(id)
    result =  json.dumps(data, indent=4, sort_keys=True, default=str)
    return result

@pharms_resource.route('/api/arduino/pharms/<string:macaddress>/boxes',methods=['GET'])
def boxesForArduino(macaddress):
    print(macaddress)
    data = boxService.boxesByPharmForArduino(macaddress)
    result =  json.dumps(data, indent=4, sort_keys=True, default=str)
    return result  