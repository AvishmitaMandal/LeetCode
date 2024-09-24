class Node:
        def __init__(self, val):
            self.prev = None
            self.next = None
            self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        newNode = Node(homepage)
        self.curr = newNode

    def visit(self, url: str) -> None:
        curr = self.curr
        newNode = Node(url)
        
        curr.next = newNode
        newNode.prev = curr
        self.curr = newNode

        print("[visit]")
        print(self.curr)
        
    def back(self, steps: int) -> str:
        node = self.curr

        while node.prev and steps:
            node = node.prev
            steps -= 1

        self.curr = node
        print("[back]")
        print(self.curr)

        return self.curr.val
        

    def forward(self, steps: int) -> str:
        node = self.curr

        while node.next and steps:
            node = node.next
            steps -= 1

        self.curr = node
        print("[forward]")
        print(self.curr)

        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)