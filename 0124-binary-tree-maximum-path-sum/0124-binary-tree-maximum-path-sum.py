# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSumUtil(self, root, max_sum):
        if root == None:
            return max_sum, 0

        if root.left == None and root.right == None:
            max_sum = max(max_sum, root.val)
            return max_sum, root.val

        res_left, res_right = 0, 0
        if root.left:
            max_sum, res_left = self.maxPathSumUtil(root.left, max_sum)

        if root.right:
            max_sum, res_right = self.maxPathSumUtil(root.right, max_sum)

        max_sum = max(max_sum, res_left + root.val + res_right)
        if root.left:
            max_sum = max(max_sum, res_left)
        if root.right:
            max_sum = max(max_sum, res_right)
        res = max(res_left + root.val, res_right + root.val, root.val)

        max_sum = max(max_sum, res)
        return max_sum, res

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -1001
        max_sum, res = self.maxPathSumUtil(root, max_sum)

        return max(max_sum, res)


        