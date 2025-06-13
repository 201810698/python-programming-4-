#self-study 11-1

inFp = None
inStr = ""

inFp = open("C:/Temp/data1.txt", "r")

lineNum = 1  

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (lineNum, inStr), end="")  
    lineNum += 1  

inFp.close()