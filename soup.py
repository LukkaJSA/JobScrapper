import requests
from bs4 import BeautifulSoup

def scrapbf (page):
	soup = BeautifulSoup(page, "html.parser")
	print(soup.prettify())

def scrap_and_write(page, file_path):
	soup = BeautifulSoup(page, "html.parser")
	file = open(file_path + 'offer.txt', "w", encoding = "utf-8")
	file2 = open(file_path + 'html.txt', "w", encoding = "utf-8")


	exp = soup.find_all(class_="tw-overflow-hidden ng-star-inserted")

	for i in range(len(exp)):
		print(exp[i].get_text())

	file2.write(str(soup.prettify()))
	file.write(str(soup.get_text()))
	file.close()
	file2.close()
