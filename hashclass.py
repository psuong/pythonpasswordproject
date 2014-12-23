#class of hashes with the first 5 digits as zero
class zeroTable:
    def __init__(self):
        self.dict = {}
    def findKey(self, key):
        isExistent = self.dict.has_key(key)
        #self.dict.get(key)
        return isExistent
    def initialInsert(self, key):
        self.dict[key] = 0
        return
    def addKey(self,key):
        valueCount = self.dict.get(key)
        self.dict[key] = valueCount + 1
        return