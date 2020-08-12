while True :
  code = input ("code: ")
  output = ""
  for letter, number in zip (list (code), [list (letter) for letter in list (code) if letter != "n"]) :
    if letter == "n" :
      output += "0000000"
    elif number = 0 :
      
    else :
      if letter == "+" :
        output += "1000000"
      if letter == "-" :
        output += "0100000"
      if letter == "*" :
        output += "1100000"
      if letter == "/" :
        output += "0010000"
      if letter == "^" :
        output += "1010000"
      if letter == "√" :
        output += "0110000"
      if letter == "g" :#get
        output += "1110000"
      if letter == "i" :#input
        output += "0001000"
      if letter == "s" :# str
        output += "1001000"
      if letter == "m" :#multi line str
        output += "0101000"
      if letter == "M" :#mappig
        output += "1101000"
      if letter == "I" :#int
        output += "0011000"
      if letter == "f" :#float
        output += "0000100"
      if letter == "l" :#list
        output += "1000100"
      if letter == "r" :#run
        output += "0100100"
      if letter == "R" :#run if
        output += "1100100"
  print (output)
    
