
from flask import Blueprint,request,json,jsonify
from user_service import UserService
from flask import jsonify,Response
from flask_cors import CORS, cross_origin

users_resource = Blueprint('users_resource',__name__)
cors = CORS(users_resource)
userService = UserService()

@users_resource.route('/api/users/',methods=['GET'])
def all(): 
    return jsonify(userService.all())

@users_resource.route('/api/users/<int:id>/',methods=['GET'])
def find(id):
    found = userService.find(id)
    if found is None:
        return Response(status=404)
    else:
        return jsonify(found)

@users_resource.route('/api/users/',methods=['POST'])
def create():
    usr = request.json['usr'] #recupero il title da oggetto json
    pwd = request.json['pwd']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    email = request.json['email']
    created = userService.create(usr,pwd,firstname,lastname,email)
    print(created)
    return Response(response=json.dumps(created),
        status=201,
        mimetype='application/json')

@users_resource.route('/api/users/<int:id>/',methods=['DELETE'])
def delete(id):
    found = userService.find(id)
    if found is None:
        return Response(status=404)
    userService.delete(id)  
    return Response(status=204)

@users_resource.route('/api/users/<int:id>/pharms',methods=['POST'])
def createPharm(id):
    found = userService.find(id)
    if found is None:
        return Response(status=404)
    name = request.json['name']
    ip = request.json['ip']
    macaddress = request.json['macaddress']
    wiocode = request.json['wiocode']
    accesspoint = request.json['accesspoint']
    password = request.json['password']
    gmt = request.json['gmt']
    created = userService.createPharm(id,name,ip,macaddress,wiocode,accesspoint,password,gmt)
    print(created)
    return Response(response=json.dumps(created),
        status=201,
        mimetype='application/json')

@users_resource.route('/api/users/<int:id>/pharms',methods=['GET'])
def pharms(id):
    return jsonify(userService.pharms(id))