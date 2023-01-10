class DataStream:

    def __init__(self, value: int, k: int):
        self.N = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool: 
        if self.value == num:
            self.N += 1   
        else:
            self.N = 0
        return self.N >= self.k
            
            
           
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)