import arrh_to_list as converter

def convertFileTobinary (fileLoc) :
	return listToBinary (
		converter.convertFileToList (fileLoc)
	)

def listToBinary (list_) :
	output = {
		"defined" : [],
		"execs" : []
	}

	for function in list_ :
		if function[0] == ":" :
			output["defined"].append (function[1])
		else :
			output["execs"].append (function)
	
	return output

if __name__ == '__main__':
	print (convertFileTobinary ("my code.arr"))