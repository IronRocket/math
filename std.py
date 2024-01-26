import collections,string,random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,data) -> None:
        self.head = Node(data)
        self.length = 1

    def append(self,data)->None:
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(data)
        self.length += 1

    def index(self,index:int)->int:
        cur = self.head
        count = 0
        while count != index and cur.next != None:
            cur = cur.next
            count += 1
        return cur.data
    
    def slice(self,start:int,stop:int)->tuple:
        items = []
        cur = self.head
        count = 0
        while count != start and cur.next != None:
            cur = cur.next
            count += 1

        count = 0
        while count != stop:
            if cur == None:
                raise Exception(f'Slice end out of range {stop}')
            items.append(cur.data)
            cur = cur.next
            count += 1
        return tuple(items)
    
    def pop(self)->int:
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = None
        self.length -= 1
        return cur.data
l = LinkedList(0)
for i in range(random.randint(1,10)):
    l.append(ord(random.choice(string.ascii_lowercase)))
for i in range(l.length):
    print(chr(l.index(i)))
print(chr(0x0023))