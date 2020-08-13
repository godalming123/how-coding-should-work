def MyCodeToMyMachine (code) :
  output = ""
  keyword = ""
  keywords = 0
  state = [0]#this is the state say if we inside a function the state would be [f]
  for letter in list (code) :
    keyword += letter
    if keywords != 0 :#if we have had keywords passed in
      if keyword == "+" :
        output += "10000"
        state += "f"
      elif keyword == "-" :
        output += "01000"
        state += "f"
      elif keyword == "*" :
        output += "11000"
        state += "f"
      elif keyword == "/" :
        output += "00100"
        state += "f"
      elif keyword == "^" :
        output += "10100"
        state += "f"
      elif keyword == "SquareRoot" :
        output += "01100"
        state += "f"
      elif keyword == "get" :
        output += "11100"
        state += "f"
      elif keyword == "input" :
        output += "00010"
        state += "f"
      elif keyword == "str" :
        output += "10010"
        state += "f"
      elif keyword == "MultiLineStr" :
        output += "01010"
        state += "f"
      elif keyword == "mapping" :
        output += "11010"
        state += "f"
      elif keyword == "Int" :
        output += "00110"
        state += "f"
      elif keyword == "float" :
        output += "00001"
        state += "f"
      elif keyword == "list" :
        output += "10001"
        state += "f"
      elif keyword == "run" :
        output += "01001"
        state += "f"
      elif keyword == "RunIf" :
        output += "11001"
        state += "f"
    elif letter == ";" :
      output += "00000"
    elif letter == " " :
      keyword = ""
      keywords += 1#there has been a keyword passed in so we add one to the keywords var
    elif letter == "n" :#n means to create a new line witch is 00000 in my code
      output += "000000"
      keyword = ""
      keywords = 0
    elif state[0] == "f" :
        output += "{10000:b}".format(ord (letter))
    else :
      if keyword == "set" :
        output += "100"
      elif keyword == "output" :
        output += "010"
      elif keyword == "run" :
        output += "110"
      elif keyword == "RunIf" :
        output += "001"
  return output
def MyCodeToBinaryFile (FileToConvert) :
  with open (FileToConvert, "r") as filecontents :
    with open ("output.exe", "w") as file2write :
      file2write.write (MyCodeToMyMachine (filecontents))
while True :
  print (MyCodeToMyMachine (input ("code: ")))
    
