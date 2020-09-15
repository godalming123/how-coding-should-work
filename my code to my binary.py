StartFuncs = ["set", "output", "run", "RunIf"]
funcs = ["+", "-", "*", "/", "^", "SquareRoot", "input", "get", "run", "RunIf"]
VarTypes = ["str", "mapping", "int", "float", "list"]

def MyCodeToMyMachine (code) :
  output = ""
  keyword = ""
  starting = True
  InFunction = []#this is the state say if we inside a function numberd 10 the state would be [10]
  inComment = False
  
  for letter in list (code) :
    #letters not to be in the keyword
    

    if letter == "/" :
      inComment = (inComment == False)

    elif inComment :#stop other elifs or elses from running when in a comment
      pass

    elif letter == " " :
      if starting :
        starting = False
        for StartFuncOn, StartFunc in enumerate (StartFuncs) :
          if keyword ==  StartFunc:
            output += str (StartFuncOn + 1)
            keyword = ""
      
      elif not starting :
        if InFunction != [] :#if we are parsing params into a function
          #output +=
          pass
        for FuncOn, func in enumerate (funcs) :
           if keyword == func :
            output += str (FuncOn + 1)
            InFunction.append (func)
    
    elif letter == "\n" :
      starting = True
      output += "0"

    else :
      #letters to be in the keyword to be checked
      
      keyword += letter
  return output

def MyCodeToBinaryFile (FileToConvert) :
  with open (FileToConvert, "r").read () as filecontents :
    return MyCodeToMyMachine ()

while True :
  print (MyCodeToMyMachine (input ("code: ")))