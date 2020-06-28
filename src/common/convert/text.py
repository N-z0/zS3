#!/usr/bin/env python3
#coding: utf-8
### 1st line allows to execute this script by typing only its name in terminal, with no need to precede it with the python command
### 2nd line declaring source code charset should be not necessary but for exemple pydoc request it



__doc__ = "provide converters for text"#information describing the purpose of this module
__status__ = "Development"#should be one of 'Prototype' 'Development' 'Production' 'Deprecated' 'Release'
__version__ = "1.0.0"# version number,date or about last modification made compared to the previous version
__license__ = "public domain"# ref to an official existing License
__date__ = "2020-09-20"#started creation date / year month day
__author__ = "N-zo syslog@laposte.net"#the creator origin of this prog,
__maintainer__ = "Nzo"#person who curently makes improvements, replacing the author
__credits__ = []#passed mainteners and any other helpers
__contact__ = "syslog@laposte.net"# current contact adress for more info about this file



import unicodedata #provides access to the Unicode Character Database (UCD)



def to_ascii(string):
	"""Replace special accents characters by their closest ASCII equivalents"""
	return unicodedata.normalize('NFKD',string).encode('ASCII','ignore').decode()


def to_utf8(string):
	"""from string format to utf8 format"""
	return string.decode('utf8')


def to_str(string):
	"""from utf8 format to string format"""
	return string.encode('utf8')
