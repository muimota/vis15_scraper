
import sys,urllib
from bs4 import BeautifulSoup
from webcache import WebCache

def parseArticle(url,webcache = None):

	"""returns a dict with information about the article"""

	if(webcache == None):
		html_doc = urllib.urlopen(url).read()
	else:
		html_doc = webcache.get(url)
	
	soup  = BeautifulSoup(html_doc)

	title = soup.select("#titulo_noticia")[0].text.strip()
	body  = soup.select("#cuerpo_noticia")[0].text.strip()

	firma = soup.select("span.firma")[0]
	
	try:
		author	= firma.find("a", rel="author").text.strip()
	except:
		author	= ""

	try:
		articlePlaces = firma.select("span.data")[0].text.strip()
		articlePlaces = articlePlaces.encode('utf8')
		articlePlaces = articlePlaces.split('/')
		#unificamos
		for i in range(len(articlePlaces)):
			articlePlace = articlePlaces[i]
			articlePlace = articlePlace.translate(None,",.")
			articlePlace = articlePlace.strip()
			articlePlaces[i] = articlePlace
			
	except:
		articlePlaces	= []

	date    = firma.select("a.actualizado")[0]['href'].split('/')[-1]

	subtitles = []
	subtitlesH2 = soup.select("#subtitulo_noticia > h2")
	for subtitle in subtitlesH2:
		subtitles.append(subtitle.text.strip())

	links = []
	linkAnchors = soup.select('div.encabezado > div.enlaces a')
	for linkAnchor in linkAnchors:
		links.append(linkAnchor['href']);

	tags = []
	tagsDiv = soup.select("div.tags")[0];
	tagsLi  = tagsDiv.select("li a")

	for li in tagsLi:
		tags.append(li.text)
	
	#remove empty strings from lists
	#https://docs.python.org/2/library/functions.html#filter
	articlePlaces	= filter(None,articlePlaces)
	subtitles 		= filter(None,subtitles)
	links			= filter(None,links)


	article = {"author":author,"title":title,"tags":tags,"subtitles":subtitles,"links":links,"url":url,"place":articlePlaces,"date":date}
	return article


def getListPagesByTag(tag):
	
	"""returns a list of listpages urls realted with the tag"""

	url = ("http://elpais.com/tag/%s/a/" % (tag))
	html_doc = urllib.urlopen(url).read()

	soup = BeautifulSoup(html_doc)
	pages = int(soup.select("div.paginacion a.boton")[0]['href'].split('/')[-1])
	urlpages = [url]
	for i in reversed(range(1,pages+1)):
		urlpages.append(url+str(i))
	return urlpages

def getArticlesFromListPage(url,webcache = None):
	
	"""returns all articles urls that are in the listpage url"""

	if(webcache == None):
		html_doc = urllib.urlopen(url).read()
	else:
		html_doc = webcache.get(url)
	
	soup = BeautifulSoup(html_doc)
	articles = []
	anchors = soup.select(".article > h2 > a")

	for anchor in anchors:
		articles.append(anchor['href'])

	return articles

