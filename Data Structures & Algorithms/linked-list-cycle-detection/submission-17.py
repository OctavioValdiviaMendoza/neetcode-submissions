# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        t1 = head
        t2 = head.next

        while t2:
            if t1.val == t2.val:
                return True
            if t1.next:
                t1 = t1.next
            if t2.next:
                t2 = t2.next.next
            else:
                return False
            
        return False
        