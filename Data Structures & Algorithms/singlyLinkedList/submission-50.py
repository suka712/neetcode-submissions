class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        i = 0

        if (self.head == None):
            return -1

        nextNode = self.head

        while (i < index):
            if (nextNode.next != None):
                nextNode = nextNode.next
                i += 1
            else:
                return -1

        return nextNode.val
            

    def insertHead(self, val: int) -> None:
        node = Node(val)
        
        if (self.head == None):
            self.head = node
            return

        node.next = self.head
        self.head = node
        

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if (self.head == None):
            self.head = node
            return
        
        nextNode = self.head
        while (nextNode.next != None):
            nextNode = nextNode.next

        nextNode.next = node

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            return False

        i = 0

        if (self.head == None):
            return False

        size = 0
        i = 0
        cur = self.head
        while cur:
            cur = cur.next
            size += 1
        if (size <= index): return False

        nextNode = self.head

        while (i < index - 1):
            if (nextNode.next):
                nextNode = nextNode.next
                i += 1
            else:
                return False
        
        if (nextNode.next and nextNode.next.next):
            nextNode.next = nextNode.next.next
            return True

        nextNode.next = None
        return True

        

    def getValues(self) -> List[int]:
        if (self.head == None):
            return []
        
        arr = []
        nextNode = self.head
        while (nextNode.next != None):
            arr.append(nextNode.val)
            nextNode = nextNode.next
        
        arr.append(nextNode.val)

        return arr
