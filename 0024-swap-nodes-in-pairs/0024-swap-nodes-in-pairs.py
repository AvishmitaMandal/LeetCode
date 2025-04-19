# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        f = head

        if head.next == None:
            return head
        s = head.next
        new_head = s

        p = None
        n = s.next
        while s:
            s.next = f
            f.next = n
            if p != None:
                p.next = s
            if n == None or n.next == None:
                break
            p = f
            f = n
            s = n.next
            n = s.next
        
        return new_head

        