class Node:
    def __init__(self, value, previos=None, forward=None):
        self.previos = previos
        self.forward = forward
        self.value = value


class Deque:
    def __init__(self):
        self.tail = None
        self.head = None
        self.mid = None
        self.len = 0
        

    def push_back(self, val):
        new_node = Node(val, None, self.tail)
        if self.len < 1:
            self.head = self.tail = self.mid = new_node
        else:
            self.tail.previos = new_node
            self.tail = new_node
            if self.len % 2 != 0:
                self.mid = self.mid.previos
        self.len += 1
        
            


    def push_forward(self, val):
        new_node = Node(val, self.head, None)
        if self.len < 1:
            self.tail = self.head = self.mid = new_node
        else:
            self.head.forward = new_node
            self.head = new_node
            if self.len % 2 == 0:
                self.mid = self.mid.forward
        self.len += 1
        
    def push_mid(self, val):
        new_node = Node(val, None, None)
        if self.len < 1:
            self.tail = self.head = self.mid = new_node
        else:
            forward = self.mid.forward
            self.mid.forward = new_node
            new_node.forward = forward
            new_node.previos = self.mid
            if forward:
                forward.previos = new_node
            self.mid = new_node
        self.len += 1
        

    def pop_back(self):
        if self.len < 1:
            return 'Error!'
        elif self.len < 2:
            val = self.tail.value
            self.tail = self.head = self.mid = None
            self.len -= 1
            return val
        else:
            val = self.tail.value
            self.tail = self.tail.forward
            self.len -= 1
            if self.len % 2 != 0:
                self.mid = self.mid.forward
            return val

    def pop_front(self):
        if self.len < 1:
            return 'Error!'
        elif self.len < 2:
            val = self.head.value
            self.tail = self.head = self.mid = None
            self.len -= 1
            return val
        else:
            val = self.head.value
            self.head = self.head.previos
            self.head.forward = None
            self.len -= 1
            if self.len % 2 == 0:
                self.mid = self.mid.previos
            return val
