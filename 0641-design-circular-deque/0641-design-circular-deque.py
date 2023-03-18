class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.stack1 = []
        self.stack2 = []
       
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

        return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.stack1) < self.k:
            self.stack1.append(value)
            return True

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

        return False
        

    def deleteLast(self) -> bool:
        if len(self.stack1) != 0:     
            self.stack1.pop()
            return True
        
        return False
        

    def getFront(self) -> int:
        if len(self.stack1) !=0:
            return self.stack1[0]
        return -1
        

    def getRear(self) -> int:
        if len(self.stack1) != 0:
            return self.stack1[-1]
        return -1
        

    def isEmpty(self) -> bool:
        return len(self.stack1) == 0
        

    def isFull(self) -> bool:
        return len(self.stack1) == self.k
        