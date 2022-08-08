import requests
from flask import Flask, request,json,render_template
import  pymysql
import db_connector

app = Flask(__name__)

#Main method is user ,and the route for the app called users/<userid>
# supported methods
@app.route('/users/<user_id>', methods=['GET'])
def user(user_id):
        request.method = 'GET'
        #calling get method
        user_name=db_connector.getfromdb(user_id)
        user_name = user_name[0]
        if user_name != "x":
            return {'status': 'ok','user_name': user_name}, 200
        else:
            return {'status': 'error', 'reason': 'no such id'} ,500


app.run(host='0.0.0.0')
#, debug=True, port=5005)


