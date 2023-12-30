class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def dequeque(self):
        if self.head:
            dummy = self.head.next
            self.head = dummy
        else:
            raise Exception("Queue is empty, cannot dequeque")

    def printLinkedList(self):
        current_node = self.head
        linked_list_str = ""
        while current_node:
            linked_list_str += str(current_node.data)
            if current_node.next:
                linked_list_str += "->"
            current_node = current_node.next
        print(linked_list_str)

# Example usage:
linked_list = Queue()
linked_list.enqueue(2)
linked_list.enqueue(4)
linked_list.enqueue(6)
linked_list.enqueue(8)
linked_list.enqueue(10)
linked_list.enqueue(12)
linked_list.printLinkedList()
linked_list.dequeque()
linked_list.printLinkedList()
linked_list.dequeque()
linked_list.printLinkedList()
linked_list.dequeque()
linked_list.printLinkedList()
