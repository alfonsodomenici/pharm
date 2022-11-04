from datetime import date, datetime, time, timedelta
import jwt
import app

SECRET_KEY = 'ITS_2022'

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return obj.__str__()
    raise TypeError (f"Type {type(obj)} not serializable")

def encode_auth_token(user_id,upn):
        """
        Generates the Auth Token
        :return: string
        """
        
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, seconds=120),
                'iat': datetime.utcnow(),
                'sub': user_id,
                'upn':upn
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    
def decode_auth_token(auth_token):
    """
    Validates the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'