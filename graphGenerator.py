# coding=utf-8

import elpais,sys,os
import cPickle as pickle
from webcache import WebCache


reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

wb = WebCache()

articleUrls = wb.listUrls();

def getArticleId(articleUrl):
	return articleUrl.split('/')[-1][:-5]

filename = 'protestas.pickle'
if(os.path.isfile(filename)):
	graph = pickle.load(open(filename,'rb'))
else:
	graph = {}

print len(articleUrls)

for articleUrl in articleUrls:
	if(articleUrl[-5:]==('.html')):
		
		articleId = getArticleId(articleUrl)
		
		if articleId in graph:
			
			print 'already parsed'
			continue

		try:
			
			article  = elpais.parseArticle(articleUrl,wb)
			#nos quedamos con los articulos que no sean de opinion y que tengan una  ciudad asociada
			if(u'España' in article['tags'] and u'Opinión' not in article['tags'] and len(article['place'])>0):
				article['links'] = map(getArticleId,article['links'])
				graph[articleId] = article

		except:
		
			print articleUrl

pickle.dump(graph,open(filename,'wb'))


