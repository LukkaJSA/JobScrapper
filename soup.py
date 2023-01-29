import requests
from bs4 import BeautifulSoup

offer_path = 'C:\\Users\\TECHMAR\\Desktop\\PROJ\\6_NOFLUFF\\output\\'

def scrapbf (page):
	soup = BeautifulSoup(page, "html.parser")
	print(soup.prettify())

def scrap_and_write(page):
	soup = BeautifulSoup(page, "html.parser")
	file = open(offer_path + 'offer.txt', "w")
	print(soup.get_text())
	file.write(soup.get_text())
	file.close()