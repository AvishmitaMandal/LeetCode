# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        slow = 7
        fast = 6

        slow = 2
        fast = 3
        '''
        if head.next == None:
            head = None
            return head

        slow, fast = head, head
        while fast.next.next and fast.next.next.next:
            fast = fast.next.next
            slow = slow.next

        new_next = slow.next.next
        slow.next = new_next

        return head

        
        