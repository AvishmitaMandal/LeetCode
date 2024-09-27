# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if root == None:
            return count

        q = deque()
        q.append([root,root.val])

        while q:
            curr = q.popleft()
            curr_node, curr_val = curr[0], curr[1]

            if curr_node.val >= curr_val:
                count += 1

            if curr_node.left:
                q.append([curr_node.left, max(curr_node.left.val,curr_val)])

            if curr_node.right:
                q.append([curr_node.right, max(curr_node.right.val,curr_val)])

        return count
        