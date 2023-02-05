from scrapp import *
import time
from soup import *
from no_fluff import *
from no_fluff_data import *


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *

#job1 = JOBLISTING()
#job1.display()


driver.get(MAIN_URL)
driver.fullscreen_window()

page_count=0
f = open(OUT_Path + "joblist.txt","w")

#Close RODO and select Testing offers
WaitUntilVisible(By.ID, RODO_locator)
WaitAndClick(By.ID, RODO_locator)
WaitAndClick(By.XPATH, Categories_locator)
WaitAndClick(By.XPATH, Testing_locator)
WaitAndClick(By.XPATH, Show_offers_locator)

#Get pages count with job listings to browse
#page_count = get_pages_count(driver)
#print("Total page count with job offerings is is {pg_count}".format(pg_count=page_count))

#Find total number of jobs on current site
elementslist = driver.find_elements(By.XPATH, "//a[contains(@id,'nfj')]")
number_of_job_offers = len(elementslist)

picturelistID = []
picturelistALL = []


job1 = JOBLISTING()
job1.display()

# Main loop to save elements
for s in range(1):
        picturelistID.clear()

        elementslist = driver.find_elements(By.XPATH, Element_locator)
        companylist = driver.find_elements(By.XPATH, Company_locator)
        listingtitle = driver.find_elements(By.XPATH, Job_title_locator)
        salary = driver.find_elements(By.XPATH, Salary_locator)
        time.sleep(0.5)

        for i in range(1):
            scrap_offer(elementslist[i],driver,job1)

        for i in range(len(elementslist)):
            driver.execute_script('arguments[0].scrollIntoView(true);', companylist[i])
            picturelist = driver.find_elements(By.XPATH, Picture_locator )
            time.sleep(0.5)
            for i in range(len(picturelist)):
                if picturelist[i].id not in picturelistID:
                    picturelistID.append(picturelist[i].id)
                    picturelistALL.append(picturelist[i])
                    GetPicture(picturelist[i],str(picturelist[i].id),OUT_Path)

        print("Ilosc elementow22")
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
#End of main loop

f.close()
driver.close()