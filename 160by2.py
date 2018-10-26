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


def login():
    driver = webdriver.Firefox(executable_path='./geckodriver')

    driver.get("http://www.160by2.com");
    timeout = 420

    try:
        WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']")))
    except TimeoutException:
        pass
	

    usernameElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("username"))

    usernameElement.send_keys("9023074222")

    
    passwordElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("password"))

    passwordElement.send_keys("3712")

    loginElement=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='ind-reg-but ind-but-butns']")))

    loginElement.click()

    print("Hlo 2")

    #print(driver.page_source)

    #//*[@id="sendSMSMsg"]
    #WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sendSMSMsg"]')))
    

    driver.get("http://www.160by2.com/")

    time.sleep(15)

    try:
        
    
        inputs=driver.find_elements_by_tag_name("textarea");


        for i in inputs:
            print("H"+i.get_attribute("id"))

        textElement=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sendSMSMsg"]')))

        print("Hlo")
        textElement.send_keys("Hello ")
        print("Hlo 4")

        numberElement=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, './/*[@id="sendSMSMsg"]')))

        numberElement.send_keys("8568993655")

        sendElement=WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name("btnsendsms"))

        sendElement.click()

        driver.get("http://www.160by2.com/Logout")
        driver.quit()

    except Exception as e:
        driver.get("http://www.160by2.com/Logout")
        driver.quit()


login()