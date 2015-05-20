from webcache import WebCache
from thingscounter import thingsCounter,getFiguresFromArticle
from bs4 import BeautifulSoup
import random,re,sys,pickle

reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

things = {}

wb  = WebCache()
filename = 'protestas4.pickle'
graph = pickle.load(open(filename,'rb'))

articleIds = graph.keys()
articleCount = 0
for articleId in articleIds:

	article = graph[articleId]

	articleThings = getFiguresFromArticle(article)
	if len(articleThings) > 0:
		article['things'] = articleThings
		print article['url']
		print articleThings
		articleCount = articleCount + 1

	for thing in articleThings:
		if thing in things:
			things[thing] = things[thing] + 1
		else:
			things[thing] = 1

print ("articles:%s article with numbers:%s" % (len(articleIds),articleCount))

f = open('things-all.csv','w')
for thing in things:
	line  = ('"%s",%s' % (thing,things[thing])) 
	f.write(line+'\n')
f.close()

filename = 'protests4.pickle'
pickle.dump(graph,open(filename,'wb'))

articleIds = graph.keys()
for articleId in articleIds:
	article = graph[articleId]
	if 'things' in article:
		print article['things']




