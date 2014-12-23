import hashlib
import re
from hashclass import zeroTable

def makeZeroDict():
    zeroDict = zeroTable()
    zeroRegex = r'[00000]'
    fname = 'zeroLinkedin.txt'
    newFile = open(fname, "w")
    with open("Linkedin.txt") as hashList:
        for hashLine in hashList:
            result = re.search(zeroRegex, hashLine)
            newFile.write(str(result))
            if result:
                password = hashLine[5::]
                zeroDict.initialInsert(password)
    return zeroDict

def checkPasswords(refDict):
    newDict = zeroTable()
    newDict = refDict.copy()
    with open ('0k most common.txt') as passwords:
        for line in passwords:
            hashedPasswords = hashlib.sha1(line)
            passwordHex = hashedPasswords.digest()
            newDict.findKey(passwordHex)


makeZeroDict()