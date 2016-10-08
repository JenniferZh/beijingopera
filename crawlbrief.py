
import urllib2
import urllib
from bs4 import BeautifulSoup as bsp
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import xml.etree.ElementTree as ET 

file = open('newactor.xml', 'w')
file.write('<root>')
actortree = ET.parse('actor.xml')
root = actortree.getroot()
for i in range(0,1000):
	print i
	actor = root[i]
	request = urllib2.Request(actor[0].text)
	response = urllib2.urlopen(request)
	html = response.read()
	soup = bsp(html)
	info = soup.find(id="article").get_text()

	#remove the useless thing in the brief info 
	info2 = soup.find(attrs={'class':'photoHolder'}).get_text()  
	info = info.replace(info2,"") 
	index = info.find(u'\u6D3B\u52A8\u5E74\u8868')
	info = info[:index]

	#store the info in the xml
	if(actor.find("info") == None):
		binfo = ET.SubElement(actor, 'info')
		binfo.text = info
	file.write(ET.tostring(actor))
file.write('</root>')
