# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTreeUtil(self, root):
        if root == None:
            return 0, 0
        
        left_dia, left_depth, right_dia, right_depth = 0,0,0,0
        if root.left:
            left_dia, left_depth = self.diameterOfBinaryTreeUtil(root.left)
        if root.right:
            right_dia, right_depth = self.diameterOfBinaryTreeUtil(root.right)

        depth = 1 + max(left_depth, right_depth)
        dia = max(left_dia, right_dia, 1+left_depth+right_depth)

        return dia, depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        dia, depth = self.diameterOfBinaryTreeUtil(root)

        return dia-1

        

        