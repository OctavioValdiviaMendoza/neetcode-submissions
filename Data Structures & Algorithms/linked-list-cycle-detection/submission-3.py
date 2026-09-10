# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        seen = set()
        curr = head
        while(curr != None):
            if curr in seen:
                return True
            else:
                seen.add(curr)
            curr = curr.next
        return False

            
        