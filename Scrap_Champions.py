import requests
from bs4 import BeautifulSoup
import re

'''
response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
'''
response = requests.get(
	url="https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%BA%D0%B8_%D0%BC%D0%B8%D1%80%D0%B0_%D0%BF%D0%BE_%D1%85%D1%83%D0%B4%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9_%D0%B3%D0%B8%D0%BC%D0%BD%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%B5",
)

soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find(id="mw-pages")
#champions = results.find_all("div", class_="mw-category-group")
champions = results.find_all("a")
print("Всего чемпионок по художественной гимнастике {}".format(len(champions)))

#for person in champions:
#	print(person.text, person.get("href"))

wiki = "https://ru.wikipedia.org"
averina = champions[2]
print(averina.text, averina.get("href"))

# Здесь мы скачиваем в суп страницу Авериной
# Тебе нужно пройти по всему списку champions по каждой чемпионке напечатать строку
# ФИО: ростб вес

response = requests.get(
	url = wiki + averina.get("href")
)

soup = BeautifulSoup(response.content, 'html.parser')
spans = soup.find_all('span')

for span in spans:
	#print(span.string)
	if span.string:
		if "см" in span.string:
			if re.match(r"[0-9]", span.string):
				print(span.string)
		if "кг" in span.string:
			if re.match(r"[0-9]", span.string):
				print(span.string)




