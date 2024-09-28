# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getOrderedList(self, root, orderedList):
        if root == None:
            return orderedList

        if root.left == None and root.right == None:
            orderedList.append(root.val)
            return orderedList

        if root.left:
            orderedList = self.getOrderedList(root.left, orderedList)

        orderedList.append(root.val)

        if root.right:
            orderedList = self.getOrderedList(root.right, orderedList)

        return orderedList

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_list = []
        ordered_list = self.getOrderedList(root, ordered_list)

        print(ordered_list)

        return ordered_list[k-1]
        