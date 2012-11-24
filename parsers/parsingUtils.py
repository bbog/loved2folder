# -*- coding: utf-8 -*-

def getValue(parentNode, childName):
	return parentNode.getElementsByTagName(childName)[0].childNodes[0].nodeValue

# credits: http://parand.com/say/index.php/2007/07/13/simple-multi-dimensional-dictionaries-in-python/
class SongDict(dict):
    def __init__(self, default=None):
        self.default = default

    def __getitem__(self, key):
        if not self.has_key(key):
            self[key] = self.default()
        return dict.__getitem__(self, key)