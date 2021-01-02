def convertFileToList (fileLoc) :
	return returnList (
		open (
			fileLoc
		).read ()
	)

def getListAtDepthAndAppend (depth, list_, itemToAppend) :
	theItemWeAddTo = "[-1]" * (depth - 1)
	theItemWeGet = theItemWeAddTo + "[-1]"

	if type (eval ("list_%s" %theItemWeGet)) is list:
		eval ("list_%s.append ('%s')" %(theItemWeGet, itemToAppend))#we can append to list
	else:
		eval ("list_%s.append (['%s'])" %(theItemWeAddTo, itemToAppend))

	return list_

def appendBlankList (depth, list_) :
	thePlaceWeAppend = "[-1]" *depth
	eval("list_%s.append([])" %thePlaceWeAppend)
	return list_
	output = [[]]
	tabs = 1
	text = ""

def returnList (code) :
	for letter in list (code):
		if letter == "\t" :#tab
			if text != "" :#tab and text defined
				output = getListAtDepthAndAppend (tabs, output, text)
				tabs = 1
				text = ""
			else :#tab
				tabs += 1

		else :
			if letter != "\n" :
				text += letter
			elif letter == "\n" :
				if text == "" :#newline and blank line prveiosly
					output = appendBlankList (tabs - 1, output)
	
	if text != "" :#we have text that hasnt been appended
		output = getListAtDepthAndAppend (tabs, output, text)
	
	return output
