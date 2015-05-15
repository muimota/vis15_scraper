# coding=utf-8

#analizes tags count in periods of time

import elpais,sys,os,pickle
from webcache import WebCache


reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

filename = 'protestas.pickle'
graph = pickle.load(open(filename,'rb'))

timeranges = [['00000000','19800000'],['19800000','19850000'],['19850000','19900000'],['19900000','19950000'],['19950000','20000000'],['20000000'
,'20050000'],['20050000','20100000'],['20100000','20150000'],['20150000','99990000']]

def tagCount(startDate,endDate):
	tags = {}

	articleIds = graph.keys()
	
	for articleId in articleIds:

		article = graph[articleId]
		if( article['date'] < startDate or article['date'] > endDate ):
			continue

		articleTags = article['tags']
		
		for tag in articleTags:
			if tag in tags:
				tags[tag] = tags[tag]+1
			else:
				tags[tag] = 1

	return tags; 

tagcounts = {}
tags = set()

for timerange in timeranges:

	tagcounts[timerange[0]] =  tagCount(timerange[0],timerange[1])

	tags = tags.union(set(tagcounts[timerange[0]].keys()))

tags = list(tags)

f = open('timetags.csv','w')

for tag in tags:

	chunks = [('"%s"' % tag)]

	for timerange in timeranges:

		if tag in tagcounts[timerange[0]]:
			tagcount = tagcounts[timerange[0]][tag]
		else:
			tagcount = 0

		chunks.append(tagcount)
		line = (',').join(map(str,chunks))
	
	f.write(line+'\n')

f.close()

# f = open('timetags.csv','w')

# for tag in tags:
# 	line = ('"%s",%s\n' % (tag.replace('"', '\\"'),tags[tag]))
# 	f.write(line);

# f.close()