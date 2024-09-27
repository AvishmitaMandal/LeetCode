# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTUtil(self, root):
        left_min, right_min, right_max, left_max = 2**31, 2**31, -(2**32), -(2**32)
        
        if root == None:
            return True, left_min, right_max

        if root.left == None and root.right == None:
            return True, root.val, root.val

        

        left_subtree, right_subtree = True, True
        if root.left:
            left_subtree, left_min, left_max = self.isValidBSTUtil(root.left)
            if root.left.val >= root.val:
                left_subtree = False
            elif root.val <= left_max:
                left_subtree = False


        if root.right:
            right_subtree, right_min, right_max = self.isValidBSTUtil(root.right)
            if root.right.val <= root.val:
                right_subtree = False
            elif root.val >= right_min:
                right_subtree = False

        if left_subtree and right_subtree:
            return True, left_min, right_max

        return False, left_min, right_min

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid, val, val = self.isValidBSTUtil(root)
        return isValid

        