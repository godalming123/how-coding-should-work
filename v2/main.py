def returnList (code) :
  output = []
  starting = False
  tabs = 0
  element = [""]

  for letter in list(code) :
    if starting :
      if letter != " ":# if we start a normal new line
        output += element
        element = [""]#reset element
        starting = False

      elif letter == " " :# if we have a tabbed newline
        tabs += 1

    if letter == "\n" :
      starting = True

    else :
      element[len(element) - 1] += letter# target the last element in elemnt and add the letter to it
    return output

with open ("v2\code to convert.txt", "r") as text :
  print (returnList (text.read()))