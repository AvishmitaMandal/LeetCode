# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def child_to_par(self, root, mp):
        if root.left is None and root.right is None:
            mp[root.val] = (0, root)
            return (0, root)

        min_dist, min_node = 1001, None
        if root.left:
            (dist_l, node_l) = self.child_to_par(root.left, mp)
            if dist_l < min_dist:
                min_dist = dist_l
                min_node = node_l
        
        if root.right:
            (dist_r, node_r) = self.child_to_par(root.right, mp)
            if dist_r < min_dist:
                min_dist = dist_r
                min_node = node_r

        min_dist += 1
        mp[root.val] = (min_dist, min_node)

        return (min_dist, min_node)


        
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        mp = {}
        (dist, node) = self.child_to_par(root, mp)

        q = deque()
        q.append(root)

        while q:
            curr_node = q.popleft()
            dist, node = mp[curr_node.val]

            if curr_node.left:
                dist_l, node_l = mp[curr_node.left.val]
                if dist_l > dist + 1:
                    mp[curr_node.left.val] = (dist+1, node)
                q.append(curr_node.left)

            if curr_node.right:
                dist_r, node_r = mp[curr_node.right.val]
                if dist_r > dist + 1:
                    mp[curr_node.right.val] = (dist+1, node)
                q.append(curr_node.right)

        dist, node = mp[k]
        return node.val
        