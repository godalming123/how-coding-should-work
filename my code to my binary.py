StartFuncs = ["set", "output", "run", "RunIf"]
funcs = ["+", "-", "*", "/", "^", "SquareRoot", "input", "get", "run", "RunIf"]
VarTypes = ["str", "mapping", "int", "float", "list"]

def MyCodeToMyMachine (code,
                       output = "", keyword = "",
                       hasntRanCommand = True,
                       InFunction = [],
                       inComment = False,
                       inHashComment = False,
                       charOn = 1,
                       lineOn = 1,
                       showDebug = True
                       ) :
  for letter in list (code) :
    def letterIs (string) :
      return (letter == string)

    #def addToOutput (input) :
    #  if showDebug:
    #    output += "ln: " + lineOn + "char: " + charOn + " "
    #
    #  output += input

    #debug features
    if showDebug :
      charOn += 1

      if letterIs("\n") :
        lineOn += 1
        charOn = 1

    #letters not to be in the keyword
    if letter == "\\" :
      inComment = (inComment == False)

    elif letter == "#" :
      inHashComment = True

    elif inComment or inHashComment :#stop other elifs or elses from running when in a comment
      if inHashComment and letter == "\n":
        inHashComment = False
    
    elif letter == " " :
      if hasntRanCommand:
        hasntRanCommand = False
        if keyword != "":
          for StartFuncOn, StartFunc in enumerate (StartFuncs) :
            if keyword ==  StartFunc:
              output += str (StartFuncOn + 1)
              keyword = ""

            #else:
            #  print ("")
      
      elif not hasntRanCommand :
        if InFunction != [] :#if we are parsing params into a function
          #output += 
          pass
        for FuncOn, func in enumerate (funcs) :
          if keyword == func :
            output +=  str (FuncOn + 1)
            InFunction.append (FuncOn)
    
    elif letter == "\n" :
      if not hasntRanCommand:
        output += "0"
      hasntRanCommand = True
      
    else :
      #letters to be in the keyword to be checked
      
      keyword += letter
  return output

def MyCodeToBinaryFile (FileToConvert) :
  with open (FileToConvert, "r") as filecontents :
    return MyCodeToMyMachine (filecontents.read ())

print (MyCodeToBinaryFile("file to convert to binary.txt"))