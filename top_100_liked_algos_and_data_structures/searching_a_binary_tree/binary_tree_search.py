class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)

    return root


def recursive_search(root, key, parent):
    if root is None:
        print("Key not found")
        return
    
    if root.data == key:
        if parent is None:
            print(f"The node with key {key} is root node")

        elif key < parent.data:
            print(f"The given key is the left of the node with key {parent.data}")

        else:
            print(f"The given key is the right node of the node with key {parent.data}")
            return 

    if key < root.data:
        recursive_search(root.left, key, root)
    else:
        recursive_search(root.right, key, root)

def iterative_search(root, key):
    curr = root
    parent = None

    if key < curr.data:
        curr = curr.left
    else:
        curr = curr.right

    if curr is None:
        print("Key not found")
        return
    
    if parent is None:
        print(f"The node with key {key} is root node")
    elif key < parent.data:
        print(f"The given key is the left node of the node with key {parent.data}")

    else:
        print(f"The given key is the right node of the node with the key {parent.data}")

keys = [15, 10, 20, 8, 12, 16, 25]
root = None
for key in keys:
    root = insert(root, key)

iterative_search(root, 25)
recursive_search(root, 25, None)
