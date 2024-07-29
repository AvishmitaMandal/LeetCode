# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        while q1 and q2:

            curr_q1 = q1.popleft()
            curr_q2 = q2.popleft()

            if curr_q1.val != curr_q2.val:
                return False

            if curr_q1.left:
                q1.append(curr_q1.left)
                if curr_q2.left:
                    q2.append(curr_q2.left)
                else:
                    return False
            elif curr_q2.left:
                return False

            if curr_q1.right:
                q1.append(curr_q1.right)
                if curr_q2.right:
                    q2.append(curr_q2.right)
                else:
                    return False
            elif curr_q2.right:
                return False

            

        if (len(q1) == 0 and len(q2) != 0) or (len(q1) != 0 and len(q2) == 0):
            return False

        return True
                

        