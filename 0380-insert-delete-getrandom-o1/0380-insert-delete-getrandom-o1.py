class RandomizedSet:

    def __init__(self):
        #use hashmap and list
        self.numsMap = {}
        self.numsList = []

    def insert(self, val: int) -> bool:
        if val not in self.numsMap:
            self.numsMap[val] = len(self.numsList)
            self.numsList.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.numsMap:
            idx = self.numsMap[val]
            lastNum = self.numsList[-1]
            self.numsList[idx] = lastNum
            self.numsList.pop()
            self.numsMap[lastNum] = idx
            del self.numsMap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.numsList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()