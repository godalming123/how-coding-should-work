from myCodingLangFor_x86 import *
from listToBinary import *
from textToList import *

def convertFile(path, function) :
	return function(open(path, "r").read())

if __name__ == '__main__':
	print (
		convertFile ("../how-coding-should-work\list.arrh", listToBinary),#list to binary
		convertFile ("../code.arr", returnList)#text to list
	)
	