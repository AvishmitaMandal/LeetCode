# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB

        while nodeA:
            lenA += 1
            nodeA = nodeA.next

        while nodeB:
            lenB += 1
            nodeB = nodeB.next

        if lenA > lenB:
            diff = lenA - lenB
            nodeA, nodeB = headA, headB
            while diff:
                nodeA = nodeA.next
                diff -= 1

        else:
            diff = lenB - lenA
            nodeA, nodeB = headA, headB
            while diff:
                nodeB = nodeB.next
                diff -= 1

        while nodeA and nodeB and nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next

        return nodeA
        