
class Stack:
    #Magic functions
    def __init__(self, lifo):
        #is_lifo is bool
        self.is_lifo = lifo
        self.root = None
        self.last = None
        self.active = None

    def __str__(self):
        node = self.root
        nodes = ''
        while node is not None:
            nodes += str(node.value) + ' '
            node = node.next

        return nodes

    def __len__(self):
        node = self.root
        counter = 0
        while node is not None:
            counter += 1
            node = node.next

        return counter

    def __iter__(self):
        self.active = None
        return self

    def __next__(self):
        if not self.active:
            self.active = self.root
        else:
            if self.active.next != None:
                self.active = self.active.next
            else:
                self.active = None
                raise StopIteration

        return self.active.value


    #Stack
    #Push based on Lifo or Fifo logic
    def push(self, value):
        if self.root is None:
            self.root = Stack.Node(value)
            self.last = self.root
            return

        if self.is_lifo:
            self.last.next = Stack.Node(value)
            self.last.next.previous = self.last
            self.last = self.last.next
        else:
            node = Stack.Node(value)
            node.next = self.root
            self.root.previous = node
            self.root = node

    #Remove the last node
    def pop(self):
        if self.last is None:
            return None

        val = self.last.value
        self.last.previous.next = None
        self.last = self.last.previous
        return val

    #Class for node of the stack
    class Node:

        def __init__(self, val):
            self.value = val
            self.next = None
            self.previous = None
