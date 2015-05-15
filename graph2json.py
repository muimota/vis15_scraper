# coding=utf-8

import sys,pickle,json
from webcache import WebCache


reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

filename = 'protestas.pickle'
graph = pickle.load(open(filename,'rb'))

tags = set()

for articleId in graph:
	
	article = graph[articleId]
	articleTags = article['tags']
	
	for tag in articleTags:
		tags.add(tag)

tags = list(tags)

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

	article['title']	 = articleOrig['title']
	article['subtitles'] = articleOrig['subtitles']
	article['place']	 = articleOrig['place']
	article['url']		 = articleOrig['url']
	date 				 = articleOrig['date']
	
	if date in articles:
		articles[date].append(article)
	else:
		articles[date] = [article]


data = {'articles':articles,'tags':tags}


json.dump(data,open('protestas.json','w'))