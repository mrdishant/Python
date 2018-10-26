import requests
import bs4
import datetime

from flask import Flask
from flask import request
import json
import os
from time import sleep
import time


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


import csv

#----------------------------------------------------------------------


phoneNumber="9023074222"
password="F2829K"


def csv_reader(file_obj,f):

    """

    Read a csv file

    """

    reader = csv.DictReader(file_obj, delimiter=',')

    for row in reader:
        f.write(row['Phone 1 - Value'].replace("-","").replace("+91","").replace("::: ","\n").replace(" ","")+","+row['Name']+"\n")
        print(row['Phone 1 - Value'].replace("-","").replace("+91","").replace("::: ","\n").replace(" ",""))

        

#----------------------------------------------------------------------

# if __name__ == "__main__":

#     csv_path = "google.csv"
#     f=open("mobiles.txt","a+")

#     with open(csv_path, "r") as f_obj:

#         csv_reader(f_obj,f)


def login():
    driver = webdriver.Firefox(executable_path='./geckodriver')

    driver.get("http://www.way2sms.com/");
    timeout = 420

    try:
        WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='mobileNo']")))
    except TimeoutException:
        pass
	

    usernameElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("mobileNo"))

    # usernameElement.send_keys("9023074222")
    usernameElement.send_keys("8568993655")
    
    passwordElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("password"))

    # passwordElement.send_keys("F2829K")
    passwordElement.send_keys("D6495C")

    loginElement=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-theme-sm btn-ls text-uppercase']")))

    loginElement.click()

    print("Hlo 2")

    #print(driver.page_source)

    #//*[@id="sendSMSMsg"]
    #WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sendSMSMsg"]')))
    time.sleep(10)

    f1=open("mobiles.txt","r");
    
    for f1 in f1.readlines():

        print(f1)
        
        if(f1.__contains__(",")):
            name=f1.split(",")[1]
            number=f1.split(",")[0]
        else:
            number=f1
            name = ""

        print(name)
        print(number)

        numberElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("toMobile"))

        numberElement.clear();
        numberElement.send_keys(number);


        # inputs=driver.find_elements_by_tag_name("input");

        # for i in inputs:
        #     print(i.text)

        textElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element(By.XPATH,'//*[@id="message"]'))
        # textElement=driver.find_element(By.XPATH,'//*[@id="message"]');

        print("Hlo")
        textElement.clear();
        
        # textElement.send_keys("May this morning be better and sweet. Better for your enemy and sweet for your friends. Good Morning!! "+name+"\nRegards Appyflow Technologies Pvt. Ltd.")
        msg="May your soul always remain filled with enthusiasm and motivation every day. Good Morning!! "+name+"\nAppyflow Technologies"
        textElement.send_keys(msg)
        print(len(msg))

        # numberElement=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, './/*[@id="sendSMSMsg"]')))

        # numberElement.send_keys("8568993655")

        
        sendElement=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sendButton"]')))

        sendElement.click()

        time.sleep(15);


    
    driver.get("http://www.way2sms.com/Logout")
    time.sleep(2)
    driver.quit()

phones=[]
recievers=[]


def main():
    loginCredentials=open("logins.txt","r");

    phones=loginCredentials.readlines()

    print(phones[0])
    
    loginCredentials.close()

    recieversList=open("mobiles.txt","r");

    recievers=recieversList.readlines()

    print(recievers[0])

    driver = webdriver.Firefox(executable_path='./geckodriver')

    driver.get("http://www.way2sms.com/");
    timeout = 420

    count=0
    recieversCount=0

    while count < len(phones):

        try:
            WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='mobileNo']")))
        except TimeoutException:
            pass
        

        usernameElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("mobileNo"))

        # usernameElement.send_keys("9023074222")
        usernameElement.send_keys(phones[count].split(",")[0])
        
        passwordElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("password"))

        # passwordElement.send_keys("F2829K")
        passwordElement.send_keys(phones[count].split(",")[1])

        count=count+1

        loginElement=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-theme-sm btn-ls text-uppercase']")))

        loginElement.click()

        print("Login username ",phones[count].split(",")[0])

        print("Login Password ",phones[count].split(",")[1])

        #print(driver.page_source)

        #//*[@id="sendSMSMsg"]
        #WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sendSMSMsg"]')))
        time.sleep(10)

        try:
            while True:

                print(recievers[recieversCount])
                f1=recievers[recieversCount]

                if(f1.__contains__(",")):
                    name=f1.split(",")[1]
                    number=f1.split(",")[0]
                else:
                    number=f1
                    name = ""

                print(name)
                print(number)

                recieversCount=recieversCount+1

                numberElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("toMobile"))

                numberElement.clear();
                numberElement.send_keys(number);


                # inputs=driver.find_elements_by_tag_name("input");

                # for i in inputs:
                #     print(i.text)

                textElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element(By.XPATH,'//*[@id="message"]'))
                # textElement=driver.find_element(By.XPATH,'//*[@id="message"]');

                print("Hlo")
                textElement.clear();
                
                # textElement.send_keys("May this morning be better and sweet. Better for your enemy and sweet for your friends. Good Morning!! "+name+"\nRegards Appyflow Technologies Pvt. Ltd.")
                msg="May you be showered with good health and success. Happy Dussehra! "+name+"\nAppyflow Technologies"
                textElement.send_keys(msg)
                print(len(msg))

                # numberElement=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, './/*[@id="sendSMSMsg"]')))

                # numberElement.send_keys("8568993655")

                
                sendElement=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sendButton"]')))

                sendElement.click()

                time.sleep(15);
            
        except Exception as e:
            driver.get("http://www.way2sms.com/Logout")
            time.sleep(10)

main()