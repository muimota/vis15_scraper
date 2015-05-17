# coding=utf-8

from webcache import WebCache
from bs4 import BeautifulSoup
import html2text
import random,re,sys,string

reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")

validLetters = string.letters+'áéíóú'+'ÁÉÍÓÚ'+'ñÑ'
#TODO:aqui habría que ir con orden para evitar casos como "dos" unidades de "mil" en vez "dos mil"
writtenNumbers = {"decena de":10,"veintena de":20,"treintena de":30,"decenas de":50,"centenar de":100,"cien":100,"doscientas":200,"doscientos":200,
	"trescientas":300,"trescientos":300,"cuatrocientas":400,"cuatrocientos":400,"quinientas":500,"quinientas":500,
	"cientos de":500,"mil":1000,"dos mil":2000,"millar de":1000,"miles de":5000,"decenas de miles":50000}

def nonExtrictThingsCounter(text):
	
	things = {}
	text = text.lower()

	for writtenNumber in writtenNumbers:
		
		try:
			index = text.find(writtenNumber+' ')
			
			if index == -1:
				continue

			if index > 0:
				if text[index-1] in validLetters:
					continue

			thing  = text[index+len(writtenNumber):].split()[0]

		except:
			continue 
	
		valid  = True
		for i in range(len(thing)):
			
			letter = thing[i]

			if letter not in validLetters:
				
				if i<len(thing)-1:
					valid = False
				else:
					thing = thing[:-1]
				break
		
		if(valid and len(thing)>2 and thing not in things):

			things[thing] = writtenNumbers[writtenNumber]

	return things

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

def getFiguresFromArticle(article):

	things = {}

	title = article['title'].encode('utf8')
	subtitles = "#".join(article['subtitles']).encode('utf8')
	body = getArticleBody(article['url'])

	things.update(nonExtrictThingsCounter(body))
	things.update(nonExtrictThingsCounter(subtitles))
	things.update(nonExtrictThingsCounter(title))

	things.update(thingsCounter(body))
	things.update(thingsCounter(subtitles))
	things.update(thingsCounter(title))
	
	return things

if __name__ == '__main__':

	wb  = WebCache()
	url = random.choice(wb.listUrls())
	url = 'http://elpais.com/diario/2006/05/13/madrid/1147519460_850215.html'
	articleBody = getArticleBody(url)

	
	print nonExtrictThingsCounter("Cientos de vecinos opuestos a los parquímetros")

