# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.s = ""

        if root == None:
            return ""
        
        q = deque()
        q.append(root)
        self.s += str(root.val) + '|'

        while q:
            temp = ""
            for x in range(len(q)):
                curr_node = q.popleft()
                if curr_node.left:
                    temp += str(curr_node.left.val) + '|'
                    q.append(curr_node.left)
                else:
                    temp += '$|'
                
                if curr_node.right:
                    temp += str(curr_node.right.val) + '|'
                    q.append(curr_node.right)
                else:
                    temp += '$|'
            self.s += temp

        print(self.s)
        return self.s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        DUMMY = -1001
        if len(data) == 0:
            return None

        expected = 1
        node_list = []

        end = 0

        while end < len(data):
            valid = 0
            temp_list = []
            for _ in range(expected):
                temp = ""
                while data[end] != '|':
                    temp += data[end]
                    end += 1
                if temp != '$':
                    valid += 1
                    temp_list.append(int(temp))
                else:
                    temp_list.append(DUMMY)
                end += 1
            node_list.append(temp_list)    
            expected = 2*valid

        print(node_list)

        root = TreeNode(node_list[0][0])

        q = deque()
        q.append(root)
        list_index = 1

        while q:
            sub_list_index = 0
            n = len(q)
            for _ in range(n):
                curr_node = q.popleft()
                left_child_val = node_list[list_index][sub_list_index]
                if left_child_val != DUMMY:
                    node = TreeNode(left_child_val)
                    curr_node.left = node
                    q.append(node)
                else :
                    curr_node.left = None
                
                sub_list_index += 1
                right_child_val = node_list[list_index][sub_list_index]
                if right_child_val != DUMMY:
                    node = TreeNode(right_child_val)
                    curr_node.right = node
                    q.append(node)
                else :
                    curr_node.right = None
                sub_list_index += 1
            list_index += 1

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))