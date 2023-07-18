class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()

root =  Node(3)
root.insert(5)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(7)
root.insert(4)
root.display()
