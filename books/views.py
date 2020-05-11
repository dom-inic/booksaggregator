from django.shortcuts import render, redirect
import requests 
from bs4 import BeautifulSoup as bs 
from books.models import Headline 

def scrape(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://residencyzone.com/"

	content = session.get(url, verify=False).content
	soup = bs(content, "html.parser")
	books = soup.find_all('div', {"class":"curation-module__item"})
	for article in books:
		main = article.find_all('a') [0]
		link = main['href']
		image_src = str(main.find('img') ['srcset']).split(" ") [-4]
		title = main['title']
		new_headline = Headline()
		new_headline.title = title
		new_headline.url = link
		new_headline.image = image_src
		new_headline.save()
	return redirect("../")


def books_list(request):
	headlines = Headline.objects.all() [::-1]
	context = {
		'object_list': headlines, 
	}
	return render(request, "books/home.html", context)



