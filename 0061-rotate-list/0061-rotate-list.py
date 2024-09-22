# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head
        
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        k = k%n
        if k == 0:
            return head

        head2, tail2 = head, head
        for x in range(n-k):
            head2 = head2.next
            if x < n-k-1:
                tail2 = tail2.next
        
        tail2.next = None


        tail = head2
        while True:
            if tail and tail.next is None:
                break
            tail = tail.next
            
        tail.next = head

        return head2


        

        


        
        