class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.nums_list = []

    def insert(self, val: int) -> bool:
        res = val not in self.hash_map

        if res:
            self.hash_map[val] = len(self.nums_list)
            self.nums_list.append(val)

        return res

    def remove(self, val: int) -> bool:
        res = val in self.hash_map

        if res:
           indx = self.hash_map[val]
           lastVal = self.nums_list[-1]

           self.nums_list[indx] = lastVal
           self.nums_list.pop()

           self.hash_map[lastVal] = indx
           self.hash_map.pop(val)

        return res

    def getRandom(self) -> int:
        return random.choice(self.nums_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()