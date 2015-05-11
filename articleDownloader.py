import elpais
from webcache import WebCache

wb = WebCache()
	
listPages = elpais.getListPagesByTag("protestas_sociales")

errorPages = []
print len(listPages)
for listPage in listPages[200:201]:

	print ("listPage %s" % listPage)
	articleUrls = elpais.getArticlesFromListPage(listPage,wb)[0]
	for articleUrl in articleUrls:
		try:
			article = elpais.parseArticle(articleUrl,wb)
			print article
		except Exception as e:
			articleUrl