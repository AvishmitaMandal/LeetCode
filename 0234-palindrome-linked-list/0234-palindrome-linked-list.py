# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev_list(self, head, even):
        prev = None 
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node

        if even:
            return prev
        
        return prev.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        even = 0
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next and fast.next.next == None:
            even = 1

        listB = slow.next
        slow.next = None
            
        listA = self.rev_list(head, even)

        nodeA, nodeB = listA, listB
        while nodeA and nodeB:
            if nodeA.val != nodeB.val:
                return False
            nodeA = nodeA.next
            nodeB = nodeB.next

        return True
        
        
        