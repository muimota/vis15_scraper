vis15_scap
==========

Scrapes news from [elpais.es](http://elpais.es) used for the project [mapas del descontento](http://mapas.muimota.net) developed during visualizar2015 at [medialabprado](http://medialab-prado.es)

What you will need
------------------

python + beautiful soup 4 .
To install bs4 I just type pip install bs4

How to use it
-------------

'''
 >>> import elpais                                                               
 >>> elpais.parseArticle('http://politica.elpais.com/politica/2015/06/02/actualidad/1433230643_116445.html')
{'date': '20150602', 'place': ['Madrid'], 'subtitles': [u'El magistrado de la Audiencia Nacional les env\xeda la citaci\xf3n antes de que pierdan su condici\xf3n de aforados'], 'links': ['http://politica.elpais.com/politica/2015/03/20/actualidad/1426849408_217445.html'], 'author': u'Fernando J. P\xe9rez', 'url': 'http://politica.elpais.com/politica/2015/06/02/actualidad/1433230643_116445.html', 'title': u'El juez imputa a los consejeros de Madrid Victoria y Figar por \u2018P\xfanica\u2019', 'tags': [u'Operaci\xf3n P\xfanica', u'Luc\xeda Figar', u'Salvador Victoria', u'Fiscal\xeda Anticorrupci\xf3n', u'Adjudicaci\xf3n contratos', u'Contratos administrativos', u'Contrataci\xf3n p\xfablica', u'Corrupci\xf3n pol\xedtica', u'Sector p\xfablico', u'Corrupci\xf3n', u'Gasto p\xfablico', u'Fiscal\xeda', u'Derecho administrativo', u'Casos judiciales', u'Poder judicial', u'Finanzas p\xfablicas', u'Pol\xedtica', u'Delitos', u'Administraci\xf3n p\xfablica', u'Econom\xeda', u'Finanzas', u'Justicia']}
'''


Webcache
--------

includes a very simple webcache based in a sqlite database. A webcache can save you lots of loading time when requesting repeatedly 



-articleDownloader.py
downloads articles tagged with a tag

-thingscounter
Tries to extract some information in the form [‘name of thing’:< amount of things >] This was used in the project to extract the amount of participants of each demonstration

-graphGenerator
Creates a pickle (ref) file with all the articles that have certain tags.

-graph Analysis
Counts all the tags and creates a cvs file 

-tagFreq
Counts tagFrequencies in different time ranges and generates a .csv file

-thingscounter 
Aims to extract from a string the amount of things mentioned
```
>>> thingscounter.thingsCounter('30 vecinos rompieron 4 farolas y cientos de almas')
{'vecinos': 30, 'farolas': 4}
>>> thingscounter.nonExtrictThingsCounter('30 vecinos rompieron 4 farolas y cientos de almas')
{'almas': 500}
```
