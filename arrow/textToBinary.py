import textToList

def convertFileTobinary (fileLoc) :
	return listToBinary (
		textToList.convertFileToList (fileLoc)
	)
	


def listToBinary (list_) :
	output = {
		"defined" : [],
		"execs" : []
	}
	vars_ = json.load (open ("converters\objects.json"))

	for function in list_ :
		if function[0] == ":" :# object is var definition
			vars_["unidentified"].append (function[1])
			output["defined"].append (function[2])
		
		else :# object is execution
			for index, deafualtFunction in enumerate (vars_["function"]) :
				if function[0] == deafualtFunction :
					output["execs"].append ([index, function[slice(1, len(function))]])
				else :
					output["execs"].append ("ERROR: could not find function %s in ram" %str (function))
	
	return output
