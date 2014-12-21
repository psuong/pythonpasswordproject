import re

yahooList = open("Yahoo.txt", "r")
#fname = raw_input("Enter a name for the file: ")
fname = "yahoocracked.txt"
newFile = open(fname, "w")
newFile.write("Line #\tEmail\tPassword")
emailRegex = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net)'
with open("Yahoo.txt") as emailList:
    for line in emailList:
        emailList = yahooList.readlines()
        emailResult = re.search(emailRegex, emailList)
        newFile.write("".join(emailList))
