# -*- coding: utf-8 -*-

import parsingUtils

from xml.dom import minidom


def parseLovedXML(xmlFile):
	xmldoc = minidom.parse(xmlFile)
	itemlist = xmldoc.getElementsByTagName('track') 

	for track in itemlist :
		title = parsingUtils.getValue(track, 'name')
		artist = track.getElementsByTagName('artist')[0]
		artist = parsingUtils.getValue(artist, 'name')
		#print title + ' - ' + artist

#parseLovedXML('loved.xml')
