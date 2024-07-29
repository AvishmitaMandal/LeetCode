# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isIdentical(self, p, q):
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

        if len(q1) == 0 and len(q2) == 0:
            return True

        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True

        if root == None and subRoot != None:
            return False

        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if curr.val == subRoot.val:
                if self.isIdentical(curr, subRoot):
                    return True

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        return False
        