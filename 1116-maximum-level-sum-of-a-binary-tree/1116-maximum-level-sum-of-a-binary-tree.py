# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -10**10
        max_level = 0
        level = 0

        q = deque()
        q.append(root)

        while q:
            total = 0 
            level += 1
            for x in range(len(q)):
                curr = q.popleft()
                total += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if total > max_sum:
                max_sum = total
                max_level = level

        return max_level
        