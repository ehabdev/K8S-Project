import requests
import os
import signal
from flask import Flask, request,json,render_template
import  pymysql
import datetime
import db_connector

app = Flask(__name__)


#Main method is user ,and the route for the app called users/<userid>
# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        #calling insert method
        #username retrived as list
        username =db_connector.inserttodb(user_name,user_id)
        #extracting the value of the username
        username=username[0]
        if username == user_name:
            return {'status': 'ok','user_added':username} ,200
        else :
            return {'status':'Error','reason':'id already exist'},500

    elif request.method == 'GET':
        #calling get method
        user_name=db_connector.getfromdb(user_id)
        user_name = user_name[0]
        if user_name != "x":
            return {'status': 'ok', 'user_name': user_name}, 200
        else:
            return {'status': 'error', 'reason': 'no such id'} ,500

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        #calling put method
        username=db_connector.updatedb(user_name,user_id)
        username=username[0]
        if username == user_name :
            return {'status': 'ok', 'user_updated':user_name}, 200
        else:
            return {'status': 'error', 'reason': 'no such id'},500

    elif request.method == 'DELETE' :
        #calling delete method
        userid=db_connector.delfromdb(user_id)
        if userid == user_id :
            return {'status': 'ok', 'user_deleted':user_id},200
        else :
            return {'status': 'error', 'reason': 'no such id'},500

@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(),signal.CTRL_C_EVENT)
        return {'status': 'ok','backend server' :'stopped'} ,200
    except Exception as e:
        print(e)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404

app.run(host='0.0.0.0')
#app.run(host='127.0.0.1', debug=True, port=5000)