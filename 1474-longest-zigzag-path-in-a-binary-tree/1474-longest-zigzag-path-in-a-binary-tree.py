# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZagRecurse(self, root, max_len):
        if root.left == None and root.right == None:
            return (0,0, max_len)

        left, right = 0, 0
        if root.left:
            (left1, right1, max1) = self.longestZigZagRecurse(root.left, max_len)
            left = 1 + right1
            max_len= max(max_len, max1)

        if root.right:
            (left2, right2, max2) = self.longestZigZagRecurse(root.right, max_len)
            right = 1 + left2
            max_len = max(max_len, max2)

        max_len = max(max_len, left, right)

        return (left, right, max_len)


    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        (left, right, max_len) = self.longestZigZagRecurse(root, max_len)

        return max_len
        