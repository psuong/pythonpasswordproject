import re

def bruteForce():
    yahooList = open("Yahoo.txt", "r")
    #allows the user to name his/her file
    fname = raw_input("Enter a name for the file (this will have .txt extension): ")
    fname.join((fname,'.txt'))
    #fname = "yahoocracked.txt"
    newFile = open(fname, "w")
    newFile.write("This is the format of the file:\nLine #\tEmail\tPassword\n\n")

    emailRegex = r'[0-9]:+[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]'
    numRegex = r'[0-9]:'
    index = 0

    with open("Yahoo.txt") as emailList:
        for line in emailList:
            index += 1
            emailList = yahooList.readlines(1)
            emailResult = re.search(emailRegex, line)
            if emailResult:
                string = line [line.index(':')::]
                lineNum = str(index)
                accountInfo = ''.join((lineNum, string))
                newFile.write(accountInfo)
    yahooList.close()
    newFile.close()

bruteForce()