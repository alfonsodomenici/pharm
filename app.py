from flask import Flask, Response, request
from db_manager import mysql
from auths_resource import auths_resource
from users_resource import users_resource
from pharms_resource import pharms_resource
from boxes_resource import boxes_resource
from flask_cors import CORS

import json

app = Flask(__name__,
            static_url_path='/', 
            static_folder='web/static',
            template_folder='web/templates')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
#cors = CORS(None, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
#cors = CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})

#db configuration
app.config['MYSQL_DATABASE_USER'] = 'pharm'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pharm'
app.config['MYSQL_DATABASE_DB'] = 'db_pharm'
app.config['MYSQL_DATABASE_HOST'] = '192.168.12.209'
app.config['SECRET_KEY'] = 'ITS_2022'

mysql.init_app(app)

app.register_blueprint(auths_resource)
app.register_blueprint(users_resource)
app.register_blueprint(pharms_resource)
app.register_blueprint(boxes_resource)

'''
@app.route('/')
def home():
    response = Response("Pharm backend Works!!!")
    return response
'''