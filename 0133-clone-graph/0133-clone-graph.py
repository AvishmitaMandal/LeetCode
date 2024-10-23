"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        node_map = {}
        new_node = Node(node.val)
        node_map[node.val] = new_node

        head = new_node

        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            if curr.val in node_map:
                new_curr = node_map[curr.val] 
            else:
                new_curr = Node(curr.val)
                node_map[curr.val] = new_curr

            for neighbor in curr.neighbors:
                if neighbor.val in node_map:
                    new_neighbor = node_map[neighbor.val]
                else:
                    new_neighbor = Node(neighbor.val)
                    node_map[neighbor.val] = new_neighbor
                    q.append(neighbor)

                new_curr.neighbors.append(new_neighbor)

        print(head)

        return head

        