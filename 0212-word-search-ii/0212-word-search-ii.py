class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] != None

    def getNode(self, ch):
        return self.links[ord(ch)-ord('a')] 

    def putNode(self, ch, node):
        self.links[ord(ch)-ord('a')] = node

    def isEnd(self):
        return self.flag == True

    def setEnd(self):
        self.flag = True

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if not node.containsKey(c):
                node.putNode(c, TrieNode())
            node = node.getNode(c)
        node.setEnd()

    def search(self, word):
        node = self.root
        for c in word:
            if not node.containsKey(c):
                return False
            node = node.getNode(c)
        if node.isEnd():
            return True
        return False

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if not node.containsKey(c):
                return False
            node = node.getNode(c)
        
        return True



class Solution:
    def findWordsBacktrack(self, board, trie, x, y, node, visited, word, res):
        if node.isEnd():
            res.add(word)
            node.flag = False
  
        m, n = len(board), len(board[0])

        visited.add((x, y))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dx, dy in directions:
            newx, newy = x+dx, y+dy
            if newx >=0 and newx < m and newy >= 0 and newy < n and (newx, newy) not in visited:
                ch = board[newx][newy]
                if node.containsKey(ch):
                    visited.add((newx, newy))
                    res = self.findWordsBacktrack(board, trie, newx, newy, node.getNode(ch), visited, word+ch, res)
                    visited.remove((newx, newy))

        return res


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = set()
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                ch = board[x][y]
                if trie.root.containsKey(ch):
                    res = set()
                    visited = set()
                    word = board[x][y]
                    res = self.findWordsBacktrack(board, trie, x, y, trie.root.getNode(ch), visited, word, res)
                    ans.update(res)

        return list(ans)


        