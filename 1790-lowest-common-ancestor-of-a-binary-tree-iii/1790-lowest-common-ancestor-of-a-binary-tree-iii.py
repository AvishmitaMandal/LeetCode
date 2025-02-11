"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_list, q_list = [p], [q]

        while p.parent != None:
            p_list.append(p.parent)
            p = p.parent

        while q.parent != None:
            q_list.append(q.parent)
            q = q.parent

        p_list.reverse()
        q_list.reverse()

        # print(len(p_list), len(q_list))

        res_node = None
        x = 0
        while x < min(len(p_list), len(q_list)) and p_list[x] == q_list[x]:
            res_node = p_list[x]
            x += 1

        return res_node

        