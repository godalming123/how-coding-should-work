import ".arrh to list.py" as converter

list_ = converter.convertFileToList (input ())

def listToBinary (list_) :
	output = {
		"defined" : [],
		"execs" : []
	}

	for function in range (list_) :
		if function[1] == ":" :
			definangVar = True
		else :
			output["execs"] += function

		if definangVar :
			pass
	
	return output
