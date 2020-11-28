import .arrh_to_list as converter

def convertFileTobinary (fileLoc) :
	return listToBinary (
		converter.convertFileToList (fileLoc)
	)

def listToBinary (list_) :
	output = {
		"defined" : [],
		"execs" : []
	}

	for function in range (list_) :
		if function[1] == ":" :
			output[defined] += function[2]
		else :
			output["execs"] += function
	
	return output

if __name__ == '__main__':
	convertFileTobinary ("my code.arr")