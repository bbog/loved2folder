# -*- coding: utf-8 -*-

import song

from xml.dom import minidom

def getValue(parentNode, childName):
	return parentNode.getElementsByTagName(childName)[0].childNodes[0].nodeValue

def parseLoved(xmlFile):
	xmldoc = minidom.parse(xmlFile)
	itemlist = xmldoc.getElementsByTagName('track') 

	for track in itemlist :
		title = getValue(track, 'title')
		artist = getValue(track, 'creator')
		#print title + ' - ' + artist

#parseLoved('CedikFlaw_lovedtracks.xspf')
