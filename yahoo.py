import re

def bruteForce():
    yahooList = open("Yahoo.txt", "r")
    #allows the user to name his/her file
    input = raw_input("Enter a name for the file (this will have .txt extension): ")
    fname = ''.join((input, '.txt'))
    #fname = "yahoocracked.txt
    newFile = open(fname, "w")
    newFile.write("This is the format of the file:\nLine #\tEmail\tPassword\n\n")
    #general case for emails
    emailRegex = r'[0-9]:+[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]'
    index = 0

    with open("Yahoo.txt") as emailList:
        for line in emailList:
            index += 1
            emailResult = re.search(emailRegex, line)
            if emailResult:
                string = line [line.index(':')::]
                lineNum = str(index)
                accountInfo = ''.join((lineNum, string))
                newFile.write(accountInfo)
    yahooList.close()
    newFile.close()

bruteForce()