# -*- coding: utf-8 -*-

import os

import id3reader

#these functions are needed to safely escape the data for the xml
from xml.sax.saxutils import escape
from xml.sax.saxutils import quoteattr

def safe_xml(str):
    return quoteattr(escape(str))

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



#makes sure you receive a valid Yes or No answer
def validYNAnswer(ans):
    if ans == 'y':
        return True
    if ans == 'Y':
        return True
    if ans == 'Yes':
        return True
    if ans == 'yes':
        return True
    if ans == 'YES':
        return True
    if ans == 'N':
        return False
    if ans == 'n':
        return False
    if ans == 'No':
        return False
    if ans == 'no':
        return False
    if ans == 'NO':
        return False

    return None



#gets the path to the music folder and parses the filelist, writing the result to songs.xml
def getPathAndParseIt():
    path = raw_input("Enter the path to your music folder: ")
    if not os.path.exists(path):
        while True:
            path = raw_input("The folder specified does not exist. Enter the path to your music folder: ")
            if not os.path.exists(path):
                break

    filelist = parse_dirs(path)

    thelist  = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    thelist += "<songs>\n"

    print "There were " + str(len(filelist)) + " files found"
    print "Please wait while the XML is built"

    for filename in filelist:     
        if filename[-4:] == ".mp3":
            try:
                id3r = id3reader.Reader(filename)
            except UnicodeDecodeError:
                artist = "None"
                title = "None"
            except IOError:
                artist = "None"
                title = "None"
            else:
                artist = ensureutf8andstring(id3r.getValue('performer'))
                title = ensureutf8andstring(id3r.getValue('title'))
    
            if artist != "None" or title != "None":
                #print (str(i) + ". " + artist + " - " + title)
                #the safe_xml function also generates the quotes
                thelist = thelist + "    <song path=" + safe_xml(filename) + " artist=" + safe_xml(artist) + " title=" + safe_xml(title) + " />\n"

    #sorted(thelist, key = str.lower)
    thelist += "</songs>\n"

    f = open('songs.xml','w')
    #thelist = thelist.encode('utf-8')
    f.write(thelist)
    f.close()
    print "songs.xml was written"

#clear the scren
clear = lambda: os.system('cls')
clear()

print ("start")

#we check to see if we already parsed the music folder
if not os.path.exists("songs.xml"):
    getPathAndParseIt()
else:
    #maybe we need to rebuild the songs list
    validationMessage = "It seems your music folder was already parsed. Do you wish to update the songs list? Y / N: "

    while True:
        reParse = raw_input(validationMessage).strip()
        if not validYNAnswer(reParse) is None:
            break

    if validYNAnswer(reParse) == True:
        getPathAndParseIt()




