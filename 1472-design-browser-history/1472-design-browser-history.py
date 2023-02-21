class ListNode:
    def __init__(self, url='', next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        
        self.head.next = newNode
        newNode.prev = self.head
        self.head = newNode

    def back(self, steps: int) -> str:
        while steps and self.head.prev:
            self.head = self.head.prev
            steps -= 1
            
        return self.head.url

    def forward(self, steps: int) -> str:
        while steps and self.head.next:
            self.head = self.head.next
            steps -= 1
            
        return self.head.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)