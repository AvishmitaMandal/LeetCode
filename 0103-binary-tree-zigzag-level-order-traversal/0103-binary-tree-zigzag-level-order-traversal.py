# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root == None:
            return result
        
        q = deque()
        q.append(root)
        level = 1

        while q:
            temp = []
            for x in range(len(q)):
                curr = q.popleft()
                temp.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if level%2 == 0:
                temp = reversed(temp)
            result.append(temp)
            level += 1

        return result

        