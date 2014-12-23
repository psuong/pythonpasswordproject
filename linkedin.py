import hashlib
import re
import copy
from hashclass import zeroTable, newTable

def makeDict():
    zeroDict = zeroTable()
    zeroRegex = r'[00000]'
    with open('Linkedin.txt') as hashList:
        for hashLine in hashList:
            result = re.match(zeroRegex, hashLine)
            newHash = hashLine.rstrip()
            if result:
                if zeroDict.isKey(newHash):
                    zeroDict.addKey(newHash)
                else:
                    zeroDict.initialInsert(newHash)
            else:
                makeNewDict(newHash)
    print 'Finished dictionaries...'
    return zeroDict

#function makes a new dictionary object for sha1 hashes with random chars
def makeNewDict(key):
    newDict = newTable()
    if key != '':
        if newDict.isKey(key):
            newDict.addKey(key)
        else:
            newDict.initialInsert(key)
    return newDict

def customInput(refDict, refDict2):
    print 'This function checks and see if a custom password exists in\nthe Linkedin.txt file.\n'
    isTrue = True
    while (isTrue):
        input = raw_input("Type in a password: ")
        password = hashlib.sha1(input)
        hexNotation = password.hexdigest()
        encrypt = ''.join(('00000', hexNotation[5::]))
        #print 'Version 1: ', hexNotation
        #print 'Version 2: ', encrypt
        if refDict.isKey(encrypt):
            refDict.getKey(encrypt)
        elif refDict2.isKey(hexNotation):
            refDict2.getKey(hexNotation)
        choice = raw_input('Do you want to continue searching? (y/n) ')
        if choice == 'y':
            isTrue = True
        else:
            isTrue = False



customInput(makeDict(), makeNewDict(''))