# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd = head
        
        if head.next == None:
            return head
        even = head.next

        list1, list2 = odd, even
        while True:
            if even.next == None:
                odd.next = None
                break
            odd_next = even.next
            odd.next = odd_next
            odd = odd_next

            if odd_next.next == None:
                even.next = None
                break
            even_next = odd_next.next
            even.next = even_next
            even = even_next

        # print(list1)
        # print(list2)

        even, odd = list2, list1
        while even and odd:
            even_next = even.next
            odd_next = odd.next
            even.next = odd
            if even_next == None:
                break
            odd.next = even_next
            even = even_next
            odd = odd_next
        
        return list2

        