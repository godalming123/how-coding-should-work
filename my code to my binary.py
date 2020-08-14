def MyCodeToMyMachine (code) :
  output = ""
  keyword = ""
  keywords = 0
  InFunction = []#this is the state say if we inside a function the state would be [f]
  for letter in list (code) :
    if letter == ";" :#char to end function
      output += "00000"
      InFunction.pop (0)
    elif letter == " " :#char to initialise function
      if keywords == 0 :
        if keyword == "set" :
          output += "100"
        elif keyword == "output" :
          output += "010"
        elif keyword == "run" :
          output += "110"
        elif keyword == "RunIf" :
          output += "001"
      
      elif keyword == "+" :
        output += "10000"
        InFunction.append ("f")
      elif keyword == "-" :
        output += "01000"
        InFunction.append ("f")
      elif keyword == "*" :
        output += "11000"
        InFunction.append ("f")
      elif keyword == "/" :
        output += "00100"
        InFunction.append ("f")
      elif keyword == "^" :
        output += "10100"
        InFunction.append ("f")
      elif keyword == "SquareRoot" :
        output += "01100"
        InFunction.append ("f")
      elif keyword == "get" :
        output += "11100"
        InFunction.append ("f")
      elif keyword == "input" :
        output += "00010"
        InFunction.append ("f")
      elif keyword == "str" :
        output += "10010"
        InFunction.append ("f")
      elif keyword == "MultiLineStr" :
        output += "01010"
        InFunction.append ("f")
      elif keyword == "mapping" :
        output += "11010"
        InFunction.append ("f")
      elif keyword == "Int" :
        output += "00110"
        InFunction.append ("f")
      elif keyword == "float" :
        output += "00001"
        InFunction.append ("f")
      elif keyword == "list" :
        output += "10001"
        InFunction.append ("f")
      elif keyword == "run" :
        output += "01001"
        InFunction.append ("f")
      elif keyword == "RunIf" :
        output += "11001"
        InFunction.append ("f")
      keyword = ""
      keywords += 1#there has been a keyword passed in so we add one to the keywords var
    
    elif letter == "n" :#n means to create a new line witch is 00000 in my code
      output += "000000"
      keyword = ""
      keywords = 0
    
    elif InFunction != [] :
      output += format(ord(letter), 'b')
    
    else :
      keyword += letter
      
  return output
def MyCodeToBinaryFile (FileToConvert) :
  with open (FileToConvert, "r") as filecontents :
    with open ("output.exe", "w") as file2write :
      file2write.write (MyCodeToMyMachine (filecontents))
while True :
  print (MyCodeToMyMachine (input ("code: ")))
