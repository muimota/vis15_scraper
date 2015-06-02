vis15_scap
==========

Scrapes news from [elpais.es](http://elpais.es) used for the project [mapas del descontento](http://mapas.muimota.net) developed during visualizar2015 at [medialabprado](http://medialab-prado.es)

What you will need
------------------

python + beautiful soup 4 .
To install bs4 I just type pip install bs4

How to use it
-------------

Parse an article Example


Webcache
--------

includes a very simple webcache based in a sqlite database. A webcache can save you lots of loading time when requesting repeatedly 

Parse all the articles tagged with a tag(Example)

*articleDownloader.py
downloads articles tagged with a tag

*thingscounter
Tries to extract some information in the form [‘name of thing’:< amount of things >] This was used in the project to extract the amount of participants of each demonstration

*graphGenerator
 creates a pickle (ref) file with all the articles that have certain tags.

*graph Analysis
 counts all the tags and creates a cvs file 

*tagFreq
 counts tagFrequencies in different time ranges and generates a .csv file

*thingscounter 
 Aims to extract from a string the amount of things mentioned
```
>>> thingscounter.thingsCounter('30 vecinos rompieron 4 farolas y cientos de almas')
{'vecinos': 30, 'farolas': 4}
>>> thingscounter.nonExtrictThingsCounter('30 vecinos rompieron 4 farolas y cientos de almas')
{'almas': 500}
```
