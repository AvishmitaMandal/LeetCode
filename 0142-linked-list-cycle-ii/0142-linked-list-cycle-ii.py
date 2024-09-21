# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return None
            
        fast, slow, slow2 = head, head, head
        hasCycle = 0

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = 1
                break

        if hasCycle == 0:
            return None

        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow


        