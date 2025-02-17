# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        level = 0
        res = []
        q = deque()
        q.append(root)

        while q:
            level += 1
            temp = []
            # odd level
            if level % 2 == 1:
                for _ in range(len(q)):
                    curr_node = q.popleft()
                    temp.append(curr_node.val)

                    if curr_node.left:
                        q.append(curr_node.left)
                    if curr_node.right:
                        q.append(curr_node.right)
            
            if level % 2 == 0:
                for _ in range(len(q)):
                    curr_node = q.pop()
                    temp.append(curr_node.val)

                    if curr_node.right:
                        q.appendleft(curr_node.right)
                    if curr_node.left:
                        q.appendleft(curr_node.left)

            res.append(temp)

        return res


                



        