class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right =None

def constructBST(arr):

    if len(arr) == 0:
        return None

    root =Node(arr[0])

    for i in range(1, len(arr)):
        if arr[i] < temp.data:
            if temp.left == None:
                temp.left = Node(arr[0])
#############
def helper(root, target):
    
    if root == None:
        return float('inf')
    
    if root.data == target:
        return target
    
    if root.data > target:
        return min(root.data, helper(root.left, target))
    
    if root.data <  target:
        return helper(root.right, target)
###################

def findCeil(root, target):
    ans = helper(root, target)
    if ans == float('inf'):
        return -1
    return ans

#######################

def ceil(root, target):
    
    if root == None :
        return float('inf')
    
    if root.data > target:
        return min(root.data, ceil(root.left, target))
    
    if root.data <=  target:
        return ceil(root.right, target)
    
def floor(root, target):
    if root == None :
        return -float('inf')
    
    if root.data >= target:
        return floor(root.left, target)
    
    if root.data <  target:
        return max(root.data, floor(root.right, target))
def predecessorSuccessor(root, key):
    c = ceil(root, key)
    f = floor(root, key)
    if c == float('inf'):
        c = -1
    if f == -float('inf'):
        f = -1
    return f,c


###############################
def findPrice(root: Node) -> int:
    if root == None:
        return -float('inf')

    if root.left == None:
        return root.data

    return findPrice(root.left)

root = constructBST([10, 7, 3,4,6,11,12,15])
