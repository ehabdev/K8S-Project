import requests
import  pymysql
import json
import random

#This moudle will verify if the userid is not exist on the DB and then will create username and then issue post and get request and then veify if the username is
#added due the userid was created at the begining of the fllow

# method getuserid(): that user id is avalible .

def getuserid():
    finduser=True
    rid = random.randint(100, 1000)
    try:

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM cAcOOBMJ8V.users where user_id=(%s);", rid)
        userid = cursor.fetchone()
        if userid == None:
            return rid
        else:
            while finduserid:
                rid = random.randint(100, 1000)
                cursor.execute("SELECT user_id FROM cAcOOBMJ8V.users where user_id=(%s);", rid)
                userid = cursor.fetchone()
                if userid == None:
                    return rid
                    finduserid=False
    except Exception as e:
        print (e)

    finally:
        cursor.close()
        conn.close()


#method to generate the username concatantion of usid+string user .
def genusername(userid):
    return ('user'+str(userid))


#post requst using generated username and password .

def postreq(userid,username):
    res = requests.post('http://127.0.0.1:5000/users/'+str(userid), json={"user_name":username})
    if res.ok:
        print(res.json())
        return id
    else:
        print(res.json())

#get requset using generated userid .
def getreq(userid):
    res = requests.get('http://127.0.0.1:5000/users/'+str(userid))
    if res.ok:
        print(res.json())
    else:
        print(res.json())

#verifing db with same username and password

def veriefy_db(userid,username):
    try:

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cAcOOBMJ8V.users where user_id=(%s);", userid)
        userid = cursor.fetchone()


        if userid[1] == username :
            print ("user name added successfully ")
        else :
            print("failed to insert user name")

    except Exception as e:
        print("test failed ")

    finally:
        cursor.close()
        conn.close()

#call method getuserid
userid=getuserid()
#call method genusername
username=genusername(userid)
#call postreq
postreq(userid,username)
#call getreq
getreq(userid)
#call verify_db
veriefy_db(userid,username)



