# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedUtil(self, root):
        if root == None:
            return True

        left_depth, right_depth = 0, 0
        leftIsBalanced, rightIsBalanced = True, True

        if root.left:
            left_depth, leftIsBalanced = self.isBalancedUtil(root.left)
        if root.right:
            right_depth, rightIsBalanced = self.isBalancedUtil(root.right)

        depth = 1 + max(left_depth, right_depth)
        isBalancedFlag = leftIsBalanced and rightIsBalanced

        if abs(left_depth-right_depth) > 1:
            isBalancedFlag = False

        return depth, isBalancedFlag 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        depth, isBalancedFlag = self.isBalancedUtil(root)

        return isBalancedFlag
        