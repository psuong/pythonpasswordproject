import hashlib
from hashclass import newTable

def formDict():
    newDict = newTable()
    with open('formspring.txt') as hashList:
        for hashLine in hashList:
            hash = hashLine.rstrip()
            newDict.addKey(hash)
    return newDict

def inputPassword(refDict):
    isTrue = True
    while (isTrue):
        input = raw_input("Type in a password: ")
        #
        for digit2 in range(0, 10):
            for digit1 in range (0,10):
                numberStr = ''.join((str(digit2), str(digit1)))
                password = ''.join((numberStr,input))
        hashedPassword = hashlib.sha256(password)
        hexNotation = hashedPassword.hexdigest()
        if refDict.iskey(hexNotation):
            refDict.getKey(hexNotation)
        choice = raw_input('Would you like to continue searching? (y/n) ')
        if choice == 'y':
            isTrue = True
        else:
            isTrue = False
    return

inputPassword(formDict())