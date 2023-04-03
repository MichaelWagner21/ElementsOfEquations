string1 = "5*17+28-72+1"
string2 = "Kotah"
operators = ("+", "-", "*", "**", "/", "=", "\\")
def NumberGrabber1(inputString):
    try:
        eval(inputString)
        numOnlyString = inputString
        for i in operators:
            numOnlyString = numOnlyString.replace(i, " ")
        numList = numOnlyString.split()
        i = 0
        while i<len(numList):
            numList[i] = int(numList[i])
            i+=1
        numList.sort()
        return numList
    except:
        print("Not a valid equation")
print (NumberGrabber1(string1))