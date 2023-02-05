from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

s = Service('C:\\geckodriver.exe')
driver = webdriver.Firefox(service=s)

import time

waittime = 4

def WaitAndClick(By_, target):
    try:
        WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By_, target)))
        driver.find_element(By_, target).click()
        time.sleep(1)
    except:
        print("Nothing to click")
    
def WaitUntilVisible(By_,target):
    try:
        WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By_, target)))
    except:
        print("Nothing to wait to")

def GetPictures(WebsiteList,iter, file_path):
    for e in range(len(WebsiteList)):
        with open(file_path + str(e) + str(iter) + '.png', 'wb') as file:
            file.write(WebsiteList[e].screenshot_as_png)

def GetPicture(target, filename, file_path):
    with open(file_path + filename + '.png', 'wb') as file:
        file.write(target.screenshot_as_png)



