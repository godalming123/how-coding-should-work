import json

from arrow import arrx_exe
from arrow import arrh_json
from arrow import json_arrx

def fileTo(type_, path) :
	fileEnding = path.split(".")[-1]
	outputFileName = path + type_

	functionOptions = {
		".arrh" : {#arrow heirachy format
			".json" : lambda x: json.dumps(textToList(x))
		},
		".arrx" : {#arrow executable
			".exe" : arrxToExe
		},
		".arr" : {#arrow codeing language
			".exe" : lambda x: arrxToExe (
				listToBinary(textToList(x))
			),
			".arrx" : lambda x: listToBinary(textToList(x))#arrow executable
		}
	}

	with open(path, "r") as fileContents :
		open (outputFileName, "w").write (
			functionOptions[fileEnding][type_](fileContents)
		)