# -*- coding: utf-8 -*-

def getValue(parentNode, childName):
	return parentNode.getElementsByTagName(childName)[0].childNodes[0].nodeValue