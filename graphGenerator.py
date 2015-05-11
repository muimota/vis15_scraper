# coding=utf-8

import elpais,sys,os,pickle
from webcache import WebCache


reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

wb = WebCache()

articleUrls = wb.listUrls();

def getArticleId(articleUrl):
	return articleUrl.split('/')[-1][:-5]

filename = 'espania.pickle'
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
			if(u'España' in article['tags'] and u'Opinión' not in article['tags']):
				article['links'] = map(getArticleId,article['links'])
				print article['tags']
			
			graph[articleId] = article

		except:
		
			print articleUrl

pickle.dump(graph,open(filename,'wb'))


