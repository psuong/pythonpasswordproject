import hashlib
import re
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
                    #checking for duplicate inserts
                    #print 'Duplicate Found!'
                    zeroDict.addKey(newHash)
                else:
                    #checking for unique inserts
                    #print 'Unique Insert'
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

def feedPasswords(refDict, refDict2):
    print '...Building passwords...'
    with open('10kmostcommon.txt') as lineList:
        for line in lineList:
            string = line.rstrip()
            password = hashlib.sha1(string)
            hexNotation = password.hexdigest()
            encryption = ''.join(('00000', hexNotation[5::]))
            if refDict.isKey(encryption):
                refDict.updateKey(encryption, string)
            elif refDict2.isKey(hexNotation):
                refDict2.updateKey(encryption, string)
    input = raw_input('Create a file name to store the passwords (file will already have a .txt extension: ')
    refDict.writetoFile(input)
    refDict2.writetoFile(input)
    return

choose = input('Choose whether to use custom password check(1) or bruteforce the passwords(2): ')
if choose == 1:
    customInput(makeDict(), makeNewDict(''))
else:
    feedPasswords(makeDict(), makeNewDict(''))