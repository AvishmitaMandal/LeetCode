class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.item_count = 0
        self.mp = {}
        
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        node.next = None 
        node.prev = None

        return node

    def insert_beginning(self, node):
        node_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = node_next
        node_next.prev = node

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            node = self.remove(node)
            self.insert_beginning(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # check in map - if present ? -> update, remove, insert in beginning
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            node = self.remove(node)
            self.insert_beginning(node)
        # if not present - check capacity overflow ? -> evict last node, insert begining 
        elif self.item_count == self.capacity:
            node = self.remove(self.tail.prev)
            del self.mp[node.key]

            new_node = Node(key, value)
            self.insert_beginning(new_node)
            self.mp[key] = new_node
        # if capacity -> insert beginning , update capacity
        else:
            new_node = Node(key, value)
            self.insert_beginning(new_node)
            self.item_count += 1
            self.mp[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)