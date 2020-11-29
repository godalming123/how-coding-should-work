import arrh_to_list as converter

deafualtVariables = [

]

def convertFileTobinary (fileLoc) :
	return listToBinary (
		converter.convertFileToList (fileLoc)
	)

def listToBinary (list_) :
	output = {
		"defined" : [],
		"execs" : []
	}
	userDeffinedVars = []

	for function in list_ :
		if function[0] == ":" :# object is var definition
			userDeffinedVars.append (function[1])
			output["defined"].append (function[2])
		else :# object is execution
			output["execs"].append (function)
	
	return output

if __name__ == '__main__':
	print (convertFileTobinary ("my code.arr"))