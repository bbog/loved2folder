# -*- coding: utf-8 -*-

import urllib

def getOnlineFile(url):
	response = urllib.urlopen(url)
	return response.read()

#http://www.last.fm/api/show/user.getLovedTracks
def getURL(user, limit=5000):
	api_key = '247b61248c7862f697cb120a9ce454ce'
	return 'http://ws.audioscrobbler.com/2.0/?method=user.getlovedtracks&user=' + user + '&limit=' + str(limit) + '&api_key=' + api_key

#url = getURL('cedikflaw')
#print getOnlineFile(url)


