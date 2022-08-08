from selenium import webdriver
from selenium.webdriver.common.by import By
import socket

def verifyfront(userid):
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    url='http://127.0.0.1:5000/users/'+str(userid)
    urlremote ='http://'+ipaddr+':5000/users/'+str(userid)

    path='C:\\Users\\idavos\\Desktop\\Devopscourse\\chromedriver.exe'


    try:
        driver = webdriver.Chrome(executable_path=path)
        driver.implicitly_wait(5)
        driver.get(url)
        driver.maximize_window()

        driverremote = webdriver.Chrome(executable_path=path)
        driverremote.implicitly_wait(5)
        driverremote.get(urlremote)
        driverremote.maximize_window()

        pslocal=driver.page_source
        psremote=driverremote.page_source





        if pslocal == psremote :
            print("validation confirmed ")
        else:
            print("validation failed ")



    except Exception as e :
            print("test failed")

    finally:

        driver.quit()
        driverremote.quit()

verifyfront(2)