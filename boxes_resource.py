
from flask import Blueprint,request,json,jsonify
from box_service import BoxService
from boxlog_service import BoxlogService
from flask import jsonify,Response
from flask_cors import CORS, cross_origin
from util import json_serial

boxes_resource = Blueprint('boxes_resource',__name__)
cors = CORS(boxes_resource)
boxService = BoxService()
boxlogService = BoxlogService()

@boxes_resource.route('/api/boxes/<int:id>/',methods=['GET'])
def find(id):
    found = boxService.find(id)
    if found is None:
        return Response(status=404)
    else:
        result = json.dumps(found, indent=4, sort_keys=True, default=str)
        return result

@boxes_resource.route('/api/boxes/<int:id>/',methods=['PATCH'])
def update(id):
    found = boxService.find(id)
    if found is None:
        return Response(status=404)
    number = request.json['number']
    color = request.json['color']
    message = request.json['message']
    timebox = request.json['timebox']
    deltatime = request.json['deltatime']
    #status = request.json['status']
    updated = boxService.update(id,number,color,message,timebox,deltatime)
    return Response(response=json.dumps(updated, default=json_serial),
        status=201,
        mimetype='application/json')

@boxes_resource.route('/api/arduino/boxes/<int:id>/',methods=['GET'])
def findForArduino(id):
    found = boxService.find(id)
    if found is None:
        return Response(status=404)
    else:
        result = json.dumps(found['status'], indent=4, sort_keys=True, default=str)
        return result

@boxes_resource.route('/api/boxes/<int:id>/',methods=['DELETE'])
def delete(id):
    found = boxService.find(id)
    if found is None:
        return Response(status=404)
    boxService.delete(id)  
    return Response(status=204)

@boxes_resource.route('/api/boxes/<int:id>/logs',methods=['POST'])
def createLog(id):
    found = boxService.find(id)
    if found is None:
        return Response(status=404)
    status = request.json['status']
    delta = request.json['delta']
    created = boxlogService.create(id,status,delta)
    print(created)
    return Response(response=json.dumps(created, indent=4, sort_keys=True, default=str),
        status=201,
        mimetype='application/json')

@boxes_resource.route('/api/boxes/<int:id>/logs',methods=['GET'])
def logs(id):
    data = boxlogService.logByBox(id)
    result =  json.dumps(data, indent=4, sort_keys=True, default=str)
    return result