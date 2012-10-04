# -*- coding: utf-8 -*-

import os

import id3reader

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

#parses all the files in a directory and returns an array with the filenames
def parse_dirs(d):
    allfiles = []
    for dirname, dirnames, filenames in os.walk(d):
        for subdirname in dirnames:
            allfiles.append(os.path.join(dirname, subdirname))
        for filename in filenames:
            allfiles.append(os.path.join(dirname, filename))
    return allfiles
	
#makes sure the value is utf8 valid and an string
def ensureutf8andstring(s):
    if isinstance(s, unicode):
        try:
            s = s.encode('utf8')
        except UnicodeDecodeError:
            s = "None"
        #s = s.encode('utf8')
    return str(s)

#clear the scren
clear = lambda: os.system('cls')
clear()

print ("start")

path = ("G:\\Muzica\\")
#test_song = ("G:\\Muzica\\The Script - Breakeven.mp3")

filelist = parse_dirs(path)

#i = 0

thelist = ""

for filename in filelist:     
    if filename[-4:] == ".mp3":
        try:
            id3r = id3reader.Reader(filename)
        except UnicodeDecodeError:
            artist = "None"
            title = "None"
        except IOError:
            arist = "None"
            title = "None"
        else:
            artist = ensureutf8andstring(id3r.getValue('performer'))
            title = ensureutf8andstring(id3r.getValue('title'))
    
        if artist != "None" or title != "None":
            #print (str(i) + ". " + artist + " - " + title)
            thelist = thelist + artist + " - " + title + "\n"

sorted(thelist, key = str.lower)

f = open('out.txt','wb')
f.write(thelist)
f.close()

"""
filelist = listdir_fullpath(path)

import id3reader


"""


"""
for filename in filelist:
    if filename[-4:] == ".mp3":
        id3r = id3reader.Reader(filename)
        artist = ensureutf8andstring(id3r.getValue('performer'))
        title = ensureutf8andstring(id3r.getValue('title'))
        if artist != "None" or title != "None":
            print (artist + " - " + title)
"""


