class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def constructBST(arr):
    root = Node(arr[0])
    for i in range(1, len(arr)):
        p = root
        while():
            if arr[i] < p.data:
                if(p.left == None):
                    p.left = Node(arr[i])
                    break
                else:
                    p = p.left
            else:
                if(p.right == None):
                    p.right = Node(arr[i])
                    break
                else:
                    p = p.right
    return root

def inorder(root):
    if root ==  None:
        return

    inorder(root.left)
    print(root.data, end="")

    inorder(root.right)

def search(root, target):
    if root == None:
        return False
    if root.data == target:
        return True

    if target > root.data:
        return search(root.right, target)
    else:
        return search(root.left, target)

 


root = constructBST([13, 3, 7, 14, 17,5])
inorder(root)
search(root, 13)


