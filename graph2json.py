# coding=utf-8

import sys,pickle,json
from webcache import WebCache


reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

filename = 'protests4.pickle'
graph = pickle.load(open(filename,'rb'))

#make a list with all the tags

tagNames = set()

for articleId in graph:
	
	article = graph[articleId]
	articleTags = article['tags']
	
	for tagName in articleTags:
		tagNames.add(tagName)

tagNames = list(tagNames)

#make a list with all the this all the things

things = set()

for articleId in graph:
	
	article = graph[articleId]
	if 'things' in article:
		articleThings = article['things']
	else:
		articleThings = {}

	for thing in articleThings:
		things.add(thing)

things = list(things)




datedArticles = {}
articleIds = graph.keys()

data = {}
places = set()

articleIndex = 0
for articleId in articleIds:
	
	datedArticle = {};
	articleOrig = graph[articleId]
	articleTags = articleOrig['tags']
	
	datedArticle['tags']=[]

	for tagName in articleTags:
		datedArticle['tags'].append(tagNames.index(tagName))


	if 'things' in articleOrig:
		
		articleThings = articleOrig['things']
		datedArticle['things'] = {}
		for thing in articleThings:
			index  = things.index(thing)
			value  = articleThings[thing]
			datedArticle['things'][index]=value
			
		#print datedArticle['things']

	datedArticle['title']	 = articleOrig['title']
	#article['subtitles'] = articleOrig['subtitles']
	datedArticle['place']	 = articleOrig['place']
	datedArticle['url']		 = articleOrig['url']
	datedArticle['date']	 = articleOrig['date']
	datedArticle['id']		 = articleId
 	date 				     = articleOrig['date']
	articleIndex = articleIndex + 1
	print datedArticle['place']
	for place in datedArticle['place']:
		places.add(place)

	if date in datedArticles:
		datedArticles[date].append(datedArticle)
	else:
		datedArticles[date] = [datedArticle]



timeline = datedArticles.keys()
timeline.sort();

articles = []
for date in timeline:
	#print datedArticles[date]
	articles = articles + datedArticles[date]


articles = dict(zip(range(len(articles)),articles))

for i in range(len(articles)):
	article = articles[i]
	article['id'] = i
#print "articles"
#print articles

tagMap = {}
for articleId in articles:
	article = articles[articleId]
	tagIds  = article['tags']
	for tagId in tagIds:
		if tagId in tagMap:
			tagMap[tagId].add(articleId)
		else:
			tagMap[tagId] = set([articleId])

for tagId in tagMap:
	tagMap[tagId] = list(tagMap[tagId])



data = {'articles':articles,'tagNames':tagNames,'tagMap':tagMap,'things':things}
json.dump(data,open('protests4.json','w'))

f = open("places.csv","w")
places = list(places)
places.sort()
for place in places:
	print place
	f.write(place+'\n')
f.close()


# articleIds = data['articles'].keys()
# print len(articleIds)
# for articleId in articleIds:
# 	article = data['articles'][articleId]

# 	if 'things' in article:
# 		print article['url']
# 		print article['things'];
# 		for thing in article['things']:
# 			print data['things'][thing]
# 			print article['things'][thing]



