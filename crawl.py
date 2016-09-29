import urllib2
import urllib
from bs4 import BeautifulSoup as bsp
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from xml.etree.ElementTree import Element, SubElement, tostring



urllist = []
# Specify the url
shengurl = 'http://history.xikao.com/directory/%E4%BA%AC%E5%89%A7/%E7%94%9F%E8%A1%8C%E6%BC%94%E5%91%98'
danurl = 'http://history.xikao.com/directory/%E4%BA%AC%E5%89%A7/%E6%97%A6%E8%A1%8C%E6%BC%94%E5%91%98'
jingurl = 'http://history.xikao.com/directory/%E4%BA%AC%E5%89%A7/%E5%87%80%E8%A1%8C%E6%BC%94%E5%91%98'
chouurl = 'http://history.xikao.com/directory/%E4%BA%AC%E5%89%A7/%E4%B8%91%E8%A1%8C%E6%BC%94%E5%91%98'
mainurl = 'http://history.xikao.com'
# This packages the request (it doesn't make it) 
urllist = [shengurl, danurl, jingurl, chouurl]
file = open('actor.xml', 'w')
root = Element('root')
for url in urllist:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()

    soup = bsp(html)

    info = soup.find_all('a', { "class" : "exist" })
    peoplelist = []
    for per in info:
        dicmap = {}
        person = SubElement(root, "person")
        href = SubElement(person, "href")
        href.text = mainurl+per['href']
        name = SubElement(person, "name")
        name.text = per['title']
file.write(tostring(root))


#request = urllib2.Request(url)

# Sends the request and catches the response
#response = urllib2.urlopen(request)

# Extracts the response
#html = response.read()




