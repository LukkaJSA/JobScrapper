from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
path = 'C:\\Users\\TECHMAR\\Desktop\\PROJ\\6_NOFLUFF\\output\\'

timeout = 5


def WaitAndClick(By, target):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By, target)))
        driver.find_element(By, target).click()
        time.sleep(0.5)
    except:
        print("Nothing to wait to")

def WaitUntilVisible(By,target):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By, target)))
        time.sleep(0.5)
    except:
        print("Nothing to wait to")

def GetPictures(WebsiteList,iter):
    for e in range(len(WebsiteList)):
        with open(path + str(e) + str(iter) + '.png', 'wb') as file:
            file.write(WebsiteList[e].screenshot_as_png)

def GetPicture(target, filename):
    with open(path + filename + '.png', 'wb') as file:
        file.write(target.screenshot_as_png)

s = Service('C:\\geckodriver.exe')

driver = webdriver.Firefox(service=s)