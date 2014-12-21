import re

yahooList = open("Yahoo.txt", "r")
#allows the user to name his/her file
#fname = raw_input("Enter a name for the file: ")
fname = "yahoocracked.txt"
newFile = open(fname, "w")
newFile.write("Line #\tEmail\tPassword")
emailRegex = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net)'
index = 0
with open("Yahoo.txt") as emailList:
    for line in emailList:
        index += 1
        emailList = yahooList.readlines(1)
        string = "".join(emailList)
        emailResult = re.search(emailRegex, line)
        if emailResult:
            newFile.write(line)