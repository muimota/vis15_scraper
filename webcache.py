import sqlite3
import urllib

class WebCache:
	
	def __init__(self,filename='htmlpages.db'):
		"""contructor, filename parameter will be where database will be stored"""
		
		self.conn = sqlite3.connect(filename)
		self.cursor = self.conn.cursor()

		# Create table
		self.cursor.execute('''CREATE TABLE if not exists htmlpages (url text UNIQUE, html text)''')

	def get(self,url):
		"""returns the content of the url, checks if it is avaliable in the webcache and if it is not will grab it"""

		#https://docs.python.org/2/library/sqlite3.html#
		self.cursor.execute('SELECT html from htmlpages WHERE url=?', (url,))
		html = self.cursor.fetchone()
		if(html == None):
			print "caching"
			html = urllib.urlopen(url).read()
			self.cursor.execute("INSERT INTO htmlpages(url,html) VALUES(?,?)",(url.decode('utf8'),html.decode('utf8'),))
			self.conn.commit()
			html = (html,)
			
		return html[0]

	def listUrls(self):
		"""lists all the urls avaiable in the webcache"""

		self.cursor.execute('SELECT url from htmlpages')
		urltuples = self.cursor.fetchall()
		urls = []

		for urltuple in urltuples:
			urls.append(urltuple[0])

		return urls



