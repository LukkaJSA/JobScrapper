### Main data
#URL adress
MAIN_URL = "Https://nofluffjobs.com"

#Output path
OUT_Path = "C:\\Users\\TECHMAR\\Desktop\\PROJ\\6_NOFLUFF\\output\\"

###Initialisation and start up
#RODO pop-up
RODO_locator = "onetrust-accept-btn-handler" #ID

#Categories - locators for pop up window with categories to select
Categories_locator = "//span[contains(text(),'Kategoria')]" #XPATH
Testing_locator = "//button[contains(text(),'Testing')]" #XPATH

###Main page with offer
#Categories window locator - action button to start offer search
Show_offers_locator = "//button[contains(text(),'Poka')]" #XPATH

#Others
Next_page_locator = "//a[contains(@class,'page-link')]" #XPATH

#Job offerings locators - main body with job offerings
Element_locator = "//a[contains(@id,'nfj')]" #XPATH
Company_locator =  "//a[contains(@id,'nfj')]//span[contains(@class,'company')]" #XPATH
Job_title_locator = "//a[contains(@id,'nfj')]//h3[contains(@class,'posting-title')]" #XPATH
Salary_locator = "//a[contains(@id,'nfj')]//span[contains(@class,'salary')]" #XPATH
Picture_locator = "//a[contains(@id,'nfj')]//img" #XPATH

###Specific offer page
#Title locator
Job_title_locator_page = "//h1[contains(@class,'font-weight-bold')]"
