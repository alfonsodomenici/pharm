from functools import wraps
from flask import Flask, request, jsonify, make_response
from util import decode_auth_token
from user_service import UserService

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            userService = UserService()
            data = decode_auth_token(token)
            current_user = userService.find(data['sub'])
            if not current_user:
                raise Exception("Invalid user") 
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated