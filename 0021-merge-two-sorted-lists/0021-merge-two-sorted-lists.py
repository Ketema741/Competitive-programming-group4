# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeRecursivelly(self, list1, list2, curnt):
        
        if  list1 == None or  list2 == None:
            if list1:
                curnt.next = list1
            if list2:
                curnt.next = list2 
            return curnt
        
        if list1.val < list2.val:
            curnt.next = list1
            curnt = curnt.next
            return self.mergeRecursivelly(list1.next, list2, curnt)
        else:
            curnt.next = list2
            curnt = curnt.next
            return self.mergeRecursivelly(list1, list2.next, curnt)
                
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curnt = dummy
        res = self.mergeRecursivelly(list1, list2, curnt)
                
        return dummy.next