#%%
# Lab 6

import random

#
# We'll define a node of a binary tree and introduce some features of Python
# classes along the way


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
        a = Node(4)
        print(a) # prints 4
        '''
        return str(self.value)



a = BST(4)
a.insert(2)
a.insert(5)
a.insert(10)
a.insert(3)
a.insert(15)

# Problem 1
# Draw (manually) the binary tree rooted in a.

    #     4
    #   /   \
    #  2     5
    #   \     \
    #    3     10
    #            \
    #             15


# Problem 2
# Write code to find the height of a Binary Search Tree

def BST_height(node):
    if (node.left == None) and (node.right == None):
        return 1
    elif (node.left != None) and (node.right == None):
        return 1 + BST_height(node.left)
    elif (node.left == None) and (node.right != None):
        return 1 + BST_height(node.right)
    return 1 + max(BST_height(node.left), BST_height(node.right))


# Problem 3

# Write code to print out the nodes of the BST using
# Breadth-First Search. How would you get the Breadth-First Traversal
# from the tree you've drawn?
# (Modify the BFS function from lecture for this problem)

def BFS_tree(node):
    q = [node]
    while len(q) > 0:
        cur_node = q.pop(0)
        print(cur_node)
        if cur_node.left != None:
            q.append(cur_node.left)
        if cur_node.right != None:
            q.append(cur_node.right)


# Problem 4

# Empirically investigate the relationship between the number of nodes in the
# tree and the height of the tree when inserting nodes with values generated
# using random.random()


def make_random_tree(n_nodes):
    '''Make a tree with n_nodes nodes by inserting nodes with values
    drawn using random.random()
    '''
    root_node = BST(random.random())
    for i in range(n_nodes-1):
        root_node.insert(random.random())
    return root_node


def height_random_tree(n_nodes):
    '''Generate a random tree with n_nodes nodes, and return its height'''
    random_tree = make_random_tree(n_nodes)
    return BST_height(random_tree)

def make_data(max_nodes):
    '''Make two lists representing the empirical relationship between
    the number of nodes in a random tree and the height of the tree.
    Generate N_TREES = 40 trees with each of
    n_nodes = 5, int(1.2*5), int(1.2^2*5), .....

    return n (a list of values of n_nodes) and h (a list of heights)

    '''
    N_TREES = 40
    n = []
    h = []

    for i in range(N_TREES):
        n_nodes = int((1.2**i) * 5)
        n.append(n_nodes)
        h.append(height_random_tree(n_nodes))

    return n, h

n, h = make_data(10000)
import matplotlib.pyplot as plt
plt.scatter(n, h)
plt.show()
# plt.savefig("trees.png") can save the data to disk

# %%
