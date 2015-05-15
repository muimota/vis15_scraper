import elpais
from webcache import WebCache

wb = WebCache()
	
listPages = elpais.getListPagesByTag("actos_protesta")

print len(listPages)
for listPage in listPages:

	print ("listPage %s" % listPage)
	
	articleUrls = elpais.getArticlesFromListPage(listPage,wb)

	for articleUrl in articleUrls:
		try:
			article = elpais.parseArticle(articleUrl,wb)
			print article
		except Exception as e:
			print "error:" + articleUrl
