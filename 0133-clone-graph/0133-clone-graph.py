"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        org_q = deque()
        new_q = deque()

        org_q.append(node)
        new_node = Node(node.val)
        new_q.append(new_node)

        explored = set()
        mp = {}
        mp[new_node.val] = new_node

        while org_q:
            org_curr = org_q.popleft()
            new_curr = new_q.popleft()
            explored.add(org_curr)
            for neighbor in org_curr.neighbors:
                if neighbor.val not in mp:
                    new_neighbor = Node(neighbor.val)
                    mp[new_neighbor.val] = new_neighbor
                else:
                    new_neighbor = mp[neighbor.val]
                new_curr.neighbors.append(new_neighbor)
                if neighbor not in explored:
                    org_q.append(neighbor)
                    new_q.append(new_neighbor)
                    explored.add(neighbor)
        
        return new_node

        