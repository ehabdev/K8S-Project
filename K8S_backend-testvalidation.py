from selenium import webdriver
from selenium.webdriver.common.by import By
import socket

def verifyfront(userid):
    f = open("k8s_url.txt", "r")
    furl=f.readline()
    furle=furl.strip()+'/users/'
    url=str(furle)+str(userid)
    path='C:\\Users\\idavos\\Desktop\\Devopscourse\\chromedriver.exe'


    try:
        driver = webdriver.Chrome(executable_path=path)
        driver.implicitly_wait(5)
        driver.get(url)
        driver.maximize_window()


        pslocal=driver.page_source
        if str(pslocal) != None :
            print(pslocal)
        else :
            print("failed to retrive the user")



    except Exception as e :
            print("test failed")

    finally:
        driver.quit()


verifyfront(2)
