# coding=utf-8

import elpais,sys,os,pickle
from webcache import WebCache


reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

filename = 'protests.pickle'
graph = pickle.load(open(filename,'rb'))

tags = {}

articleIds = graph.keys()
print len(articleIds)

for articleId in articleIds:
	
	article = graph[articleId]
	articleTags = article['tags']
	for tag in articleTags:
		if tag in tags:
			tags[tag] = tags[tag]+1
		else:
			tags[tag] = 1

f = open('tags.csv','w')

for tag in tags:
	line = ('"%s",%s\n' % (tag.replace('"', '\\"'),tags[tag]))
	f.write(line);

f.close()
