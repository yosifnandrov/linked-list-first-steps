class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def printlist(self):
        if not self.head:
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def inside(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def insertion(self,prev,data):
        if not self.inside(prev):
            raise Exception(f"{prev} not in the list")
        current = self.head
        new_node = Node(data)
        while current:
            if current.data == prev:
                new_node.next = current.next
                current.next = new_node
            current = current.next

    def delete(self,data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        while current:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next





lst = LinkedList()

for i in range(1,11):
    lst.push(i)

lst.insertion(1,20)

print(lst.inside(5))
lst.delete(5)
lst.printlist()
