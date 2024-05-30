# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3 = ListNode()
        cur1, cur2, cur3 = l1, l2, l3

        while cur1 or cur2:

            if cur1 and cur2:
                num = carry + cur1.val + cur2.val
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1 :
                num = carry + cur1.val
                cur1 = cur1.next
            else :
                num = carry + cur2.val
                cur2 = cur2.next

            carry = num // 10
            cur3.val = num % 10

            if cur1 or cur2:
                new_node = ListNode()
                cur3.next = new_node
                cur3 = cur3.next

        if carry != 0:
            cur3.next = ListNode(carry)

        return l3

        