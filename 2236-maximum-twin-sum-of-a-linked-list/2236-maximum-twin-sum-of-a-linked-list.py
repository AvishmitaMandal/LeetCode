# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        6 -> 5 -> 4 -> 3 -> 2 -> 1

        6 -> 5 -> 4 -> 1 -> 2 -> 3
        -> find mid-point
        -> reverse and attach the right half
        -> set the second pointer to the center

        Finding the mid-point
        6 -> 5 -> 4 -> 3 -> 2 -> 1
        slow = 3
        fast = None

        Reversing
        None <- 3 <- 2 <- 1
        prev = 3
        curr = 3
        next = 2

        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        '''

        slow, fast = head, head
        while fast.next.next:
            fast = fast.next.next
            slow = slow.next

        ptr = self.reverseLL(slow.next)
        slow.next = ptr

        max_twin = 0
        curr = head
        while ptr:
            total = curr.val + ptr.val
            max_twin = max(max_twin, total)
            curr = curr.next
            ptr = ptr.next

        return max_twin
        