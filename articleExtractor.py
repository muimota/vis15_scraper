from webcache import WebCache
from thingscounter import thingsCounter
from bs4 import BeautifulSoup
import random,re,sys,pickle

reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

things = {}

wb  = WebCache()
filename = 'protestas.pickle'
graph = pickle.load(open(filename,'rb'))

articleIds = graph.keys()

for articleId in articleIds:

	url = graph[articleId]['url']
	html_doc = wb.get(url)
	soup  = BeautifulSoup(html_doc)
	article_body = soup.select('#cuerpo_noticia')
	article_body = re.sub('<[^<]+?>', '', str(article_body))
	
	title = graph[articleId]['title']
	subtitles = "#".join(graph[articleId]['subtitles'])

	articleThings = thingsCounter(article_body)
	
	print articleThings

	for thing in articleThings:
		if thing in things:
			things[thing] = things[thing] + 1
		else:
			things[thing] = 1

f = open('things-body.csv','w')
for thing in things:
	line  = ('"%s",%s' % (thing,things[thing])) 
	f.write(line+'\n')

f.close()


