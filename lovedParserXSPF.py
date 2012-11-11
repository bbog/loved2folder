# -*- coding: utf-8 -*-

import parsingUtils

from xml.dom import minidom

def parseLovedXSPF(xmlFile):
	xmldoc = minidom.parse(xmlFile)
	itemlist = xmldoc.getElementsByTagName('track') 

	for track in itemlist :
		title = parsingUtils.getValue(track, 'title')
		artist = parsingUtils.getValue(track, 'creator')
		#print title + ' - ' + artist

#parseLovedXSPF('CedikFlaw_lovedtracks.xspf')
