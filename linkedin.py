import hashlib
import re
import copy
from hashclass import zeroTable

def makeZeroDict():
    zeroDict = zeroTable()
    zeroRegex = r'[00000]'
    fname = 'zeroLinkedin.txt'
    newFile = open(fname, "w")
    with open("Linkedin.txt") as hashList:
        for hashLine in hashList:
            result = re.search(zeroRegex, hashLine)
            if result:
                newHash = hashLine[5::]
                if zeroDict.findKey(newHash):
                    zeroDict.addKey(newHash)
                else:
                    zeroDict.initialInsert(newHash)
    return zeroDict

def checkPasswords(refDict):
    newDict = zeroTable()
    newDict = copy.copy(refDict)
    with open('10k most common.txt') as passwordList:
        for line in passwordList:
            password = hashlib.sha1(line)
            newDict.findKey(password.hexdigest())
            newDict.getKey(password.hexdigest())

makeZeroDict()
checkPasswords(makeZeroDict())

string = '123456'
key = hashlib.sha1(string)
print key.hexdigest()