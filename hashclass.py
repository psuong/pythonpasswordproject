import os
MAXFILESIZE = 50000000
#class of hashes with the first 5 digits as zero
class zeroTable:
    def __init__(self):
        self.dict = {}
    def isKey(self, key):
        doesExist = self.dict.has_key(key)
        return doesExist
    def getKey(self, key):
        print 'Key: ', key
        print 'Password found!'
        return key
    def initialInsert(self, key):
        value = 'NULL'
        self.dict[key] = value
        return
    def addKey(self, key):
        value = 'Duplicate found!'
        self.dict[key] = value
        return
    def updateKey(self, key, original):
        password = ''.join(('Password: ', original))
        self.dict[key] = password
        #print password
        return
    def writetoFile(self, fname):
        counter = 0
        fileName = ''.join((fname, '.txt'))
        newFile = open(fileName, 'a')
        inputSize = input('Input a file size in megabyte: ')
        inputSize *= 1000000
        if inputSize > MAXFILESIZE:
            inputSize = MAXFILESIZE
        for key, value in self.dict.iteritems():
            if self.dict.get(key) != 'NULL':
                password = ''.join((':\t', value))
                valueInfo = ''.join((password, '\n'))
                info = ''.join((key, valueInfo))
                if os.stat(fileName).st_size < inputSize:
                    newFile.write(info)
                else:
                    print 'Creating file of size ', os.stat(fileName).st_size, ' bytes'
                    newFile.close()
                    counter += 1
                    appendName = ''.join((str(counter), '.txt'))
                    fileName = ''.join((fname, appendName))
                    newFile = open(fileName, 'w')
                    newFile.write(info)

#2nd dictionary for hashes whose 1st 5 digits != 0
class newTable:
    def __init__(self):
        self.dict = {}
    def isKey(self, key):
        doesExist = self.dict.has_key(key)
        return doesExist
    def getKey(self, key):
        print 'Key: ', key
        print 'Password found!'
        return key
    def initialInsert(self, key):
        self.dict[key] = 0
        return
    def addKey(self, key):
        valueCount = self.dict.get(key)
        self.dict[key] = valueCount + 1
        return
    def updateKey(self, key, original):
        password = ''.join(('Password: ', original))
        self.dict[key] = password
        #print password
        return
    def writetoFile(self, fname):
        counter = 0
        fileName = ''.join((fname, '.txt'))
        newFile = open(fileName, 'a')
        inputSize = input('Input a file size in megabyte: ')
        inputSize *= 1000000
        if inputSize > MAXFILESIZE:
            inputSize = MAXFILESIZE
        for key, value in self.dict.iteritems():
            if self.dict.get(key) != 'NULL':
                password = ''.join((':\t', value))
                valueInfo = ''.join((password, '\n'))
                info = ''.join((key, valueInfo))
                if os.stat(fileName).st_size < inputSize:
                    newFile.write(info)
                else:
                    print 'Creating file of size ', os.stat(fileName).st_size, ' bytes'
                    newFile.close()
                    counter += 1
                    appendName = ''.join((str(counter), '.txt'))
                    fileName = ''.join((fname, appendName))
                    newFile = open(fileName, 'w')
                    newFile.write(info)