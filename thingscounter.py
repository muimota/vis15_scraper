# coding=utf-8

from webcache import WebCache
from bs4 import BeautifulSoup
import html2text
import random,re,sys,string

reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

validLetters = string.letters+'áéíóú'+'ÁÉÍÓÚ'+'ñÑ'

#cuenta cosas 
def thingsCounter(text):
	#http://stackoverflow.com/a/4289557
	things = {}
	numbers = re.findall('\\b\\d+\\.?\\d+\\b', text)
	index = 0;

	for number in numbers:
		
		try:
			index = text.find(number,index)+len(number)
			thing  = text[index:].split()[0]
		except:
			continue 

		valid  = True
		for i in range(len(thing)):
			letter = thing[i]

			if letter not in validLetters:
				if i<len(thing)-1:
					#print ">>"+thing
					valid = False
				else:
					thing = thing[:-1]
				break

		#print (thing,number,)
		if(valid and len(thing)>2 and thing not in things):
			things[thing] = int(number.replace('.',''))
		
	return things


def getArticleBody(url):
	wb  = WebCache()
	html = wb.get(url)
	soup  = BeautifulSoup(html)
	article = soup.select('#cuerpo_noticia')
	article = re.sub('<[^<]+?>', '', str(article))
	return article



if __name__ == '__main__':

	wb  = WebCache()
	url = random.choice(wb.listUrls())
	url = 'http://elpais.com/diario/2006/01/13/cvalenciana/1137183477_850215.html'
	articleBody = getArticleBody(url)

	print thingsCounter(articleBody)


