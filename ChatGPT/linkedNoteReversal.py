# This is a singly linked list reversal

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head

        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


ll = LinkedList()
ll.add("A")
ll.add("B")
ll.add("C")

ll.print_list()
ll.reverse()
ll.print_list()
