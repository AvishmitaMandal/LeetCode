class Node:
        def __init__(self, val):
            self.next = None
            self.val = val

class MyCalendar:

    def __init__(self):
        self.isEmpty = True
        self.head = None 

    def isOverlap(self, event1, event2):
        if event1[1] > event2[0]:
            return True
        return False

    def book(self, start: int, end: int) -> bool:
        event = [start, end]
        
        # Just 1 node
        if self.isEmpty:
            newNode = Node(event)
            self.head = newNode
            self.isEmpty = False
            return True

        curr = self.head
        prev = None

        while curr:
            if event[1] < curr.val[1]:
                # First element
                if prev == None:
                    if self.isOverlap(event, curr.val):
                        return False
                    else:
                        newNode = Node(event)
                        newNode.next = curr
                        self.head = newNode
                        return True
                
                # Between element
                else:
                    if self.isOverlap(prev.val, event) or self.isOverlap(event, curr.val):
                        return False
                    else:
                        newNode = Node(event)
                        newNode.next = curr
                        prev.next = newNode
                        return True

            elif event[1] == curr.val[1]:
                return False
            else:
                prev = curr
                curr = curr.next

        # end of the list
        if self.isOverlap(prev.val, event):
            return False
        else:
            newNode = Node(event)
            prev.next = newNode

        return True

        

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)