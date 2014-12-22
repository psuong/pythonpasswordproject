# The Yahoo had no hashes to compare, it was reading off a text file and scrapping the data.
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
                #creates a substring for the original account info (email:password)
                string = line [line.index(':')::]
                accountInfo = ''.join((str(index), string))
                newFile.write(accountInfo)
    #close both files
    yahooList.close()
    newFile.close()

bruteForce()