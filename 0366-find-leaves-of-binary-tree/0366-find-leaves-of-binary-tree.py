# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, node):
        if node.left == None and node.right == None:
            return True

        return False

    def findLeavesUtil(self, root):
        if self.isLeaf(root):
            root_val = root.val
            root = None
            return [root_val]

        temp = []

        if root.left:
            if self.isLeaf(root.left):
                temp.append(root.left.val)
                root.left = None
            else:
                temp += self.findLeavesUtil(root.left)

        if root.right:
            if self.isLeaf(root.right):
                temp.append(root.right.val)
                root.right = None
            else:
                temp += self.findLeavesUtil(root.right)

        return temp


    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        while root:
            temp = self.findLeavesUtil(root)
            print(temp)
            res.append(temp)
            if temp == [root.val]:
                break
            # print(res)

        return res
        