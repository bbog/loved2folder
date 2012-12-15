# -*- coding: utf-8 -*-

# IMPORT

# handles the folder/file parsing
import os
# handles reading the songs' ID3 tags
import id3reader
# used to import our custom inc folders
import sys
sys.path.insert(0, 'D:/Github/loved2folder/inc')
sys.path.insert(1, 'D:/Github/loved2folder/parsers')
# the XSPF file format parser
import lovedParserXSPF
# used to copy the loved songs to a new folder
import shutil
# handles exceptions
import errno
#these functions are needed to safely escape the data for the xml
from xml.sax.saxutils import escape
from xml.sax.saxutils import quoteattr


# METHODS


def safe_xml(str):
    return quoteattr(escape(str))


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


# parses all the files in a directory and returns an array with the filenames
def parse_dirs(d):
    allfiles = []
    for dirname, dirnames, filenames in os.walk(d):
        for subdirname in dirnames:
            allfiles.append(os.path.join(dirname, subdirname))
        for filename in filenames:
            allfiles.append(os.path.join(dirname, filename))
    return allfiles


# makes sure the value is utf8 valid and an string
def ensureutf8andstring(s):
    if isinstance(s, unicode):
        try:
            s = s.encode('utf8')
        except UnicodeDecodeError:
            s = "None"
        #s = s.encode('utf8')
    return str(s)


# we make sure the destination folder of the loved tracks exists
def makePathOk(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


#parses the songs from the given folder and checks each song to see if it's loved or not
def searchForLovedSongs(searchForLovedSongs):
    path = raw_input("Enter the path to your music folder: ")
    if not os.path.exists(path):
        while True:
            path = raw_input("The folder specified does not exist. Enter the path to your music folder: ")
            if not os.path.exists(path):
                break

    destination = raw_input("Enter the path to destination folder (the loved songs will be copyied there): ")
    makePathOk(destination)

    filelist = parse_dirs(path)

    print "There were " + str(len(filelist)) + " files found"
    print "Please wait while the songs are verified (it might take a while)"

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
                if lovedSongs[artist][title] == 1:
                    try: 
                        shutil.copy(filename, destination)
                    except:
                        print '"' + artist + ' - ' + title + '" could not be copied'
                    else:
                        print '"' + artist + ' - ' + title + '" was successfully copied'

    print "parsing done"

#clear the scren
clear = lambda: os.system('cls')
clear()

print ("start")

lovedSongs = lovedParserXSPF.parseLovedXSPF('CedikFlaw_lovedtracks.xspf')

searchForLovedSongs(lovedSongs)
