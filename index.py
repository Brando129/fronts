
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# first_node = Node(607)
# print(first_node)
# print(first_node.data)

# SLL Class
class SLL:
    def __init__(self, head):
        self.head = head

    # Classmethod for adding a new node.

    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self



    def display(self):
        runner = self.head
        node = 1
        while runner:
            print(f'This is node {node}, it has data/value of: {runner.data}')
            runner = runner.next
            node += 1
        return self


    def remove_front(self):
        if self.head:
            self.head = self.head.next
        return self


    def add_front(self, data):
        if self.head != None:
            new_node = Node(data)
            temp = self.head
            self.head = new_node
            self.head.next = temp
            return self

new_sll = SLL(Node(607))
new_sll.add(99).add(2).add('Julio').add('True')

new_sll.remove_front()
new_sll.display()