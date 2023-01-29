from scrapp import *
import time
from soup import *
from no_fluff import *

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *

driver.get("Https://nofluffjobs.com")
driver.fullscreen_window()

page_count=0
f = open("C:\\Users\\TECHMAR\\Desktop\\PROJ\\6_NOFLUFF\\output\\joblist.txt","w")

WaitAndClick(By.ID, "onetrust-accept-btn-handler")
WaitAndClick(By.XPATH, "//span[contains(text(),'Kategoria')]")
WaitAndClick(By.XPATH, "//button[contains(text(),'Testing')]")
WaitAndClick(By.XPATH, "//button[contains(text(),'Poka')]") #Show results

page_count = get_pages_count(driver)
print("Total page count with job offerings is is {pg_count}".format(pg_count=page_count))

#Find total number of jobs on single site
elementslist = driver.find_elements(By.XPATH, "//a[contains(@id,'nfj')]")
number_of_job_offers = len(elementslist)

picturelistID = []
picturelistALL = []

# Main loop to save elements
for s in range(1):
        picturelistID.clear()
        actions = ActionChains(driver)

        elementslist = driver.find_elements(By.XPATH, "//a[contains(@id,'nfj')]")
        companylist = driver.find_elements(By.XPATH, "//a[contains(@id,'nfj')]//span[contains(@class,'company')]")
        listingtitle = driver.find_elements(By.XPATH, "//a[contains(@id,'nfj')]//h3[contains(@class,'posting-title')]" )
        salary = driver.find_elements(By.XPATH, "//a[contains(@id,'nfj')]//span[contains(@class,'salary')]")

        for i in range(3):
            go_to_offer(elementslist[i],driver)

        for i in range(len(elementslist)):
            driver.execute_script('arguments[0].scrollIntoView(true);', companylist[i])
            picturelist = driver.find_elements(By.XPATH, "//a[contains(@id,'nfj')]//img")
            time.sleep(0.5)
            for i in range(len(picturelist)):
                if picturelist[i].id not in picturelistID:
                    picturelistID.append(picturelist[i].id)
                    picturelistALL.append(picturelist[i])
                    GetPicture(picturelist[i],str(picturelist[i].id))

        print("Ilosc elementow")
        print(len(picturelistALL))
        print(len(elementslist))

        
        #print(str(listingtitle[i].text.encode('utf-8', 'ignore')))
        #print("\n")

        #f.write(bytes(companylist[i].text, 'utf-8').decode('utf-8', 'ignore'))
        #f.write(";")
        #f.write(str(listingtitle[i].text.encode('utf-8', 'ignore')))
        #f.write(";")
        #f.write(salary[i].text)
        #f.write("\n")

        WaitAndClick(By.XPATH, "//span[contains(text(),'»')]")
        scrapbf(driver.page_source)
#End of main loop

f.close()
#driver.close()