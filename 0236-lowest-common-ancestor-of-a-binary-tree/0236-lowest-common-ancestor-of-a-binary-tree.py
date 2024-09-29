# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque;

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        par_map = {}
        par_map[root] = None

        qu = deque()
        qu.append(root)

        while qu:
            curr_node = qu.popleft()
            if curr_node.left:
                par_map[curr_node.left] = curr_node
                qu.append(curr_node.left)
            if curr_node.right:
                par_map[curr_node.right] = curr_node
                qu.append(curr_node.right)

        q_list, p_list = [], []
        
        while q:
            q_list.append(q)
            q = par_map[q]

        while p:
            p_list.append(p)
            p = par_map[p]

        x, y = len(q_list)-1, len(p_list)-1
        last_common_parent = None

        while q_list[x] == p_list[y]:
            last_common_parent = q_list[x]
            x -= 1
            y -= 1

        return last_common_parent

        
