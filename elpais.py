import urllib
import sys
from bs4 import BeautifulSoup

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def parseArticle(url):
	html_doc = urllib.urlopen(url).read()

	soup  = BeautifulSoup(html_doc)

	title = soup.select("#titulo_noticia")[0].text.strip()
	body  = soup.select("#cuerpo_noticia")[0].text.strip()

	firma = soup.select("span.firma")[0]
	try:
		author = firma.find("a", rel="author").text.strip()
	except:
		author = ""
	try:
		place	= firma.select("span.data")[0].text.strip()
	except:
		place  = ""
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

	article = {"author":author,"title":title,"tags":tags,"subtitles":subtitles,"links":links,"url":url,"place":place,"date":date}
	return article


def getListPagesByTag(tag):
	
	url = ("http://elpais.com/tag/%s/a/" % (tag))
	html_doc = urllib.urlopen(url).read()

	soup = BeautifulSoup(html_doc)
	pages = int(soup.select("div.paginacion a.boton")[0]['href'].split('/')[-1])
	urlpages = [url]
	for i in reversed(range(1,pages+1)):
		urlpages.append(url+str(i))
	return urlpages

def getArticlesFromListPage(url):
	
	html_doc = urllib.urlopen(url).read()

	soup = BeautifulSoup(html_doc)
	articles = []
	anchors = soup.select(".article > h2 > a")

	for anchor in anchors:
		articles.append(anchor['href'])

	return articles


listPages = getListPagesByTag("protestas_sociales")

errorPages = []

for listPage in listPages[10:15]:

	print ("listPage %s" % listPage)
	articleUrls = getArticlesFromListPage(listPage)
	for articleUrl in articleUrls:
		try:
			parseArticle(articleUrl)
		except Exception as e:
			print articleUrl


#print(len(articleUrls))

