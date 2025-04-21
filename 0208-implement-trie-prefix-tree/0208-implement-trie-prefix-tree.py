class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containsKey(self, c):
        return self.links[ord(c)-ord('a')] != None

    def putNode(self, c, node):
        self.links[ord(c)-ord('a')] = node

    def getNode(self, c):
        return self.links[ord(c)-ord('a')]

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag == True

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.containsKey(c):
                node.putNode(c, TrieNode())
            node = node.getNode(c)
        node.setEnd()
        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.containsKey(c):
                return False
            node = node.getNode(c)
        if node.isEnd():
            return True
        return False  

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.containsKey(c):
                return False
            node = node.getNode(c)

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)