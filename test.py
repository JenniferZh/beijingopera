
import urllib2
import urllib
from bs4 import BeautifulSoup as bsp
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import xml.etree.ElementTree as ET 

actortree = ET.parse('actor.xml')
root = actortree.getroot()
for i in root:
	if (i.find("info") == None):
		print "xixi"