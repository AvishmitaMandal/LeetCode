# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        INVALID = 10**9 + 1
        mp = {}
        mp[root] = TreeNode(INVALID)
        qu = deque()
        qu.append(root)

        while qu:
            for _ in range(len(qu)):
                node = qu.pop()
                if node.left:
                    mp[node.left] = node
                    qu.append(node.left)
                if node.right:
                    mp[node.right] = node
                    qu.append(node.right)

        p_list, q_list = [], []

        while p.val != INVALID:
            p_list.append(p)
            p = mp[p]

        while q.val != INVALID:
            q_list.append(q)
            q = mp[q]

        lca_node = TreeNode(INVALID)
        ptr1, ptr2 = len(p_list)-1, len(q_list)-1

        while ptr1 >= 0 and ptr2 >= 0 and p_list[ptr1] == q_list[ptr2]:
            lca_node = p_list[ptr1]
            ptr1 -= 1
            ptr2 -= 1

        return lca_node
        