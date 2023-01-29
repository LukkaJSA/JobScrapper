import requests
from bs4 import BeautifulSoup

def scrapbf (page):
	soup = BeautifulSoup(page, "html.parser")
	print(soup.prettify())
