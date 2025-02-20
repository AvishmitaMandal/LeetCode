# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp

        ptr1, ptr2 = list1, list2

        ptr1_prev = None
        while ptr1 and ptr2:
            while ptr1.next and ptr2.val > ptr1.next.val:
                ptr1 = ptr1.next

            ptr1_next = ptr1.next
            ptr2_next = ptr2.next
            ptr1.next = ptr2
            ptr2.next = ptr1_next

            ptr1_prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2_next

        if ptr2:
            ptr1_prev.next = ptr2

        return list1


        

        