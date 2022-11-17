from flask import Blueprint,request,json,jsonify,make_response
from flask import jsonify,Response
from flask_cors import CORS, cross_origin
from user_service import UserService
from util import encode_auth_token, decode_auth_token

auths_resource = Blueprint('auths_resource',__name__)
cors = CORS(auths_resource)
userService = UserService()

@auths_resource.route('/api/auths/login',methods=['POST'])
def login():
    usr = request.json['usr'] 
    pwd = request.json['pwd']
    found = userService.findByUsrPwd(usr,pwd)
    if found is None:
        responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
        return make_response(jsonify(responseObject)), 404
    else:
        token = encode_auth_token(found['id'],found['usr'])
        if token:
            responseObject = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'token': token.decode('UTF-8')
            }
            return make_response(jsonify(responseObject)), 200