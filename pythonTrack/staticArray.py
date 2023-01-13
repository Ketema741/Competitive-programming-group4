class StaticArrays: 
 def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
    self.arr = arr
    self.length = length
    self.capacity = capacity
 def insertEnd(self, value):
    if self.length < self.capacity:
        self.arr[self.length] = value
        self.length += 1
    

 def removeEnd(self):
    self.arr[self.length] = 0
    self.length -= 1

 def insertMiddle(self, index, value):
     if self.length < self.capacity:
        for i in range(index, self.length - 1):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = value
        self.length += 1
    
 def removeMiddle(self, index):
     if self.length != 0:
        for i in range(index, self.length - 1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.length] = 0
        self.length -= 1
 def printArr(self):
     print(self.arr)
 # write your code here
