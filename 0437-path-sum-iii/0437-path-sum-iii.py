# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_traversal(self, root, target):
        if root.left == None and root.right == None:
            return [root.val], int(root.val == target)

        left_list, right_list = [], []
        count_left, count_right = 0, 0
        if root.left:
            left_list, count_left = self.dfs_traversal(root.left, target)

        if root.right:
            right_list, count_right = self.dfs_traversal(root.right, target)

        count = count_left + count_right
        left_list.extend(right_list)

        for x in range(len(left_list)):
            left_list[x] += root.val
            if left_list[x] == target:
                count += 1

        left_list.append(root.val)
        if root.val == target:
            count += 1

        print(left_list, count)
        return left_list, count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0

        pathlist, count = self.dfs_traversal(root, targetSum)

        return count
        