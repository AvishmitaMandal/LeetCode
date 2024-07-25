# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap = {}
        nodeA, nodeB = headA, headB

        while nodeA:
            hashmap[nodeA] = 1
            nodeA = nodeA.next

        while nodeB:
            if nodeB in hashmap:
                return nodeB
            nodeB = nodeB.next

        return None
        