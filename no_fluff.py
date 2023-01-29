from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import *
import time
from scrapp import *

def get_pages_count(drv):

	pages = drv.find_elements(By.XPATH, "//a[contains(@class,'page-link')]")
	pg_count = 0
	# Find total number of job pages
	for n in range(len(pages)):
		print(pages[n].text)
		try:
			if pg_count<int(pages[n].text):
				pg_count=int(pages[n].text)				
		except:
			print("not comparable")
	return pg_count


def go_to_offer(element,drv):
	
	#Store the original window handler
	original_window = driver.current_window_handle
	
	#Check for other windows open
	assert len(driver.window_handles) == 1

	#Click the element go to page and wait for site to load

	element.send_keys(Keys.SHIFT, Keys.ENTER)
	time.sleep(3)
	print("@@@")

	print(EC.number_of_windows_to_be(2))

	# Loop through until we find a new window handle
	for window_handle in driver.window_handles:
	    if window_handle != original_window:
	        driver.switch_to.window(window_handle)
	        break

	WaitUntilVisible(By.XPATH, "//button[contains(text(),'Aplikuj')]")
	time.sleep(4)
	
	#Close the tab or window
	driver.close()

    #Switch back to the old tab or window
	driver.switch_to.window(original_window)