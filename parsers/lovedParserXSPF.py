# -*- coding: utf-8 -*-

import parsingUtils

from xml.dom import minidom
from collections import defaultdict

# returns a custom song dictionary
# dict[artist][title] = 1 is the standard entry
# we can use it to check if a song is loved (if dict[song's artist][song's title] is 1, the song is loved)
def parseLovedXSPF(xmlFile):
	xmldoc = minidom.parse(xmlFile)
	itemlist = xmldoc.getElementsByTagName('track') 
	
	#lovedSongsDict = parsingUtils.SongDict(dict)
	lovedSongsDict = defaultdict(lambda: defaultdict(dict))


	for track in itemlist :
		title = parsingUtils.getValue(track, 'title')
		artist = parsingUtils.getValue(track, 'creator')
		lovedSongsDict[artist][title] = 1

	return lovedSongsDict
