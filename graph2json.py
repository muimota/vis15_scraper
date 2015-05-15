# coding=utf-8

import sys,pickle,json
from webcache import WebCache


reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

filename = 'protests.pickle'
graph = pickle.load(open(filename,'rb'))

#make a list with all the tags all the tags

tags = set()

for articleId in graph:
	
	article = graph[articleId]
	articleTags = article['tags']
	
	for tag in articleTags:
		tags.add(tag)

tags = list(tags)

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




articles = {}
articleIds = graph.keys()

data = {}


for articleId in articleIds:
	
	article = {};
	articleOrig = graph[articleId]
	articleTags = articleOrig['tags']
	
	article['tags']=[]

	for tag in articleTags:
		article['tags'].append(tags.index(tag))


	if 'things' in articleOrig:
		
		articleThings = articleOrig['things']
		article['things'] = {}
		for thing in articleThings:
			index  = things.index(thing)
			value  = articleThings[thing]
			article['things'][index]=value
			

	article['title']	 = articleOrig['title']
	article['subtitles'] = articleOrig['subtitles']
	article['place']	 = articleOrig['place']
	article['url']		 = articleOrig['url']
	date 				 = articleOrig['date']
	
	if date in articles:
		articles[date].append(article)
	else:
		articles[date] = [article]


data = {'articles':articles,'tags':tags,'things':things}
json.dump(data,open('protests.json','w'))

articleIds = data['articles'].keys()
print len(articleIds)
for articleId in articleIds:
	articles = data['articles'][articleId]
	for article in articles:
		if 'things' in article:
			print article['url']
			for thing in article['things']:
				print data['things'][thing]
				print article['things'][thing]



