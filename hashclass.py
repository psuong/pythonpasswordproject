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
        self.dict[key] = 0
        return
    def addKey(self, key):
        valueCount = self.dict.get(key)
        self.dict[key] = valueCount + 1
        return


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