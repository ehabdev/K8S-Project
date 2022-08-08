import requests
import json

def backend_stop(servername ):
    req=requests.get(servername)
    print(req)
    if req.ok:
        print(req.json())



urlbackend='http://127.0.0.1:5000/stop_server'
backend_stop(urlbackend)



# def frondend_stop(servername ):
#     req=requests.get(servername)
#     print(req)
#     if req.ok:
#         print(req.json())
#
# urlfrontend='http://127.0.0.1:5001/stop_server'
# frondend_stop(urlfrontend)
