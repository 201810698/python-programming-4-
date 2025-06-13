#self-study 11-3

outFp = None
outStr = ""

outFp = open("C:/Temp/data2.txt", "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 씀 ---")


outFp = None
outStr = ""

fName = input("파일명을 입력하세요 : ")
outFp = open(fName, "r")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("--- %s 파일에 정상적으로 저장되었음 ---" % fileName)
