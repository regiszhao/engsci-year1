#%%

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''
        node.insert(5) is the same as BST.insert(node, 5)
        We use this when recursively calling, e.g. self.left.insert
        '''
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def __repr__(self):
        '''The string representation of a node.
        Here, we convert the value of the node to a string and make that
        the representation.
        We can now use
        a = BST(4)
        print(a) # prints 4
        '''
        return str(self.value)

def find_largest(node):
    if node == None:
        return None
    if node.right == None:
        return node
    if node.right.value == "deleted":
        if node.right.left == None:
            return node
        if node.right.left:
            return find_largest(node.right.left)
        
    else:
        return find_largest(node.right)

def delete_largest(node):
    largest = find_largest(node)
    largest.value = "deleted"
    return

def third_largest(node):
    for i in range(2):
        delete_largest(node)
    return find_largest(node).value

# %%
