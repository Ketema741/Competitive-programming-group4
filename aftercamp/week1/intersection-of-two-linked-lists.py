# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_set = set()

        root1 = headA
        root2 = headB

        while root1 or root2:
            if root1 in hash_set:
                return root1
            if root1:
                hash_set.add(root1)
                root1 = root1.next

            if root2 in hash_set:
                return root2

            if root2:
                hash_set.add(root2)
                root2 = root2.next

        return None