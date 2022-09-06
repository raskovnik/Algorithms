class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):

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
          
    def traverse(self, root):
        result = []
        if root is not None:
            result.append(root.data)
            result = result + self.traverse(root.left)
            result = result + self.traverse(root.right)

        return result
