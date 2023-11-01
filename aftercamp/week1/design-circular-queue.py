class ListNode:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        curr = ListNode(value, self.tail, self.tail.prev)
        self.tail.prev.nxt = curr
        self.tail.prev = curr
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head.nxt = self.head.nxt.nxt
        self.head.nxt.prev = self.head
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()