# -*- coding: utf-8 -*-

import song

from xml.dom import minidom

def parseSongs(xmlFile):
	xmldoc = minidom.parse(xmlFile)
	itemlist = xmldoc.getElementsByTagName('song') 
	print len(itemlist)
	print itemlist[0].attributes['title'].value
	for s in itemlist :
		print s.attributes['artist'].value

parseSongs('songs.xml')
