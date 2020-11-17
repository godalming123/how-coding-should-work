def deleteLastElementOfListAndGetItsValue (list, depth):
  gottens = [list]
  for i in range(depth):
    gottens += gottens[-1][-1:].pop()
  return gottens

def reconstructList (gotten):
  original = []
  for i in range(gotten) :
    pass


def returnList (code) :
  output = {
    "object definitions" : [],
    "stuff to run" : []
  }
  elementBeingAppended = []
  entered = False
  tabs = 0
  depthOfAppending = []
  state = "run stuff"
  keyword = ""

  for letter in list (code):
    if letter == ";" :#letter to end tree element
      depthOfAppending -= 1

    elif letter == "=" :#we are defining a variable
      state = "definig var"

    elif letter == "\n" :
      if state == "definig var":
        output["object definitions"] += keyword

      elif state == "run stuff" :
        output["stuff to run"] += elementBeingAppended
        elementBeingAppended = []

      state == "run stuff"#reset state for newline

    elif letter == " " :#new item in element
      if state == "run stuff":#this means we are creating a list to run
        elementBeingAppended += keyword


    else :
      keyword += letter
      #output[elementOn] += letter

  return output

def convertStringIntoList (string = "") :
  actualString = string[::-1]
  tabs = 0
  for letter in list (actualString):
    if letter == "\tab" :
      tabs += 1

with open ("v2\code to convert.txt", "r") as text :
  print (returnList (text.read()))

#print (reternLastList_(["hi", "my list"]))
