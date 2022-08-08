import  pymysql
import datetime

#inserttodb :this method will accept userid and username as input and retrieve  the username will return error message that user is already exist  .

def inserttodb(user_name,user_id):
    try:
        datetime_object = datetime.datetime.now()
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
        userid = cursor.fetchone()
        if userid != None:
            return "duplicate user"

        else:
            cursor.execute("INSERT into cAcOOBMJ8V.users (user_name,user_id,creation_date) VALUES (%s,%s,%s)",(user_name, user_id, datetime_object))
            cursor.execute("SELECT user_name FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
            conn.autocommit(True)
            username = cursor.fetchone()
            return username


    except Exception as e:
        print (e)

    finally:
        cursor.close()
        conn.close()

#getfromdb:this method will accept userid  inpout and retrive the username in case of the user is exist else it will return error message user is not exist  .

def getfromdb(user_id):
        try:
            conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB',
                                   db='cAcOOBMJ8V')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
            userid = cursor.fetchone()
            if userid == None:
                return "x"
            else:
                cursor.execute("SELECT user_name FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
                username = cursor.fetchone()
                return username

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

#updatedb:this method will accept userid and username as inpout and retrive the  updated username in case of the user is exist else it will return error message user is not exist  .
def updatedb(user_name,user_id):
    try:

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        conn.autocommit(True)
        cursor.execute("SELECT user_id FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
        userid = cursor.fetchone()
        if userid == None:
            return "user not found"

        else:
            cursor.execute("UPDATE cAcOOBMJ8V.users SET user_name = (%s) WHERE user_id = (%s)",(user_name,user_id))
            cursor.execute("SELECT user_name FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
            conn.autocommit(True)
            username = cursor.fetchone()
            return username

    except Exception as e:
        return (e)

    finally:
        cursor.close()
        conn.close()

#delfromdb:this method will accept userid  input and retrieve the userid after deleteing the recoed related to  it  in case of the user not exist   will return error message user is not exist  .

def delfromdb(user_id):
    try:

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB',db='cAcOOBMJ8V')
        cursor = conn.cursor()
        conn.autocommit(True)
        cursor.execute("SELECT * FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
        userid = cursor.fetchone()
        if userid == None:
            return "user not found"

        else:
            conn.autocommit(True)
            cursor.execute("DELETE FROM cAcOOBMJ8V.users WHERE user_id=(%s)", user_id)
            return user_id

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
