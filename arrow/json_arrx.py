import json
from arrow import arrh_json
	
def listToBinary (list_) :
	output = {
		"execs" : [],
		"defined" : []
	}

	def equal (value):
		output["defined"] += eval(value)

	vars_ = json.load (open ("arrow/objects.json"))

	for item in list_ :
		try :
			eval(
				format(
					"%s (%s)", item[0],
					", ".join(
						item[slice(
							1, len(item)
						)])
					)
			)
		except :
			pass
			
	
	return output
