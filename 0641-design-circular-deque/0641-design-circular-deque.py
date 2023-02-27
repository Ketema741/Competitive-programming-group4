class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.stack1 = []
        self.stack2 = []
        self.l = 0
        self.r = 0
        

    def insertFront(self, value: int) -> bool:
        if len(self.stack1)< self.k:
            for i in self.stack1[::-1]:
                self.stack2.append(i)
            self.stack1.clear()
            self.stack1.append(value)
            for i in self.stack2[::-1]:
                self.stack1.append(i)
            self.stack2.clear()
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.stack1) < self.k:
            self.stack1.append(value)
            return True
        else:
            return False
        


    def deleteFront(self) -> bool:
        if len(self.stack1) > 0:
            for i in self.stack1[::-1]:
                self.stack2.append(i)
            self.stack1.clear()
            self.stack2.pop()
            for i in self.stack2[::-1]:
                self.stack1.append(i)
            self.stack2.clear()
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if len(self.stack1) != 0:     
            self.stack1.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if len(self.stack1) !=0:
            return self.stack1[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if len(self.stack1) != 0:
            return self.stack1[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return True if len(self.stack1)==0 else False
        

    def isFull(self) -> bool:
        return True if len(self.stack1)== self.k else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()