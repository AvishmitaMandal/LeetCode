# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        par_hash = {}
        par_hash[root] = None
        
        qu = deque()
        qu.append(root)

        while qu:
            curr = qu.popleft()

            if curr.left:
                qu.append(curr.left)
                par_hash[curr.left] = curr

            if curr.right:
                qu.append(curr.right)
                par_hash[curr.right] = curr

        p_list, q_list = [p], [q]
        curr_p, curr_q = p, q

        while True:
            node = par_hash[curr_p]
            if node is None:
                break
            else:
                p_list.append(par_hash[curr_p])
                curr_p = par_hash[curr_p]

        while True:
            node = par_hash[curr_q]
            if node is None:
                break
            else:
                q_list.append(par_hash[curr_q])
                curr_q = par_hash[curr_q]

        temp_hash = {}

        for n in p_list:
            temp_hash[n] = 1

        for m in q_list:
            if m in temp_hash:
                return m

        return None



        