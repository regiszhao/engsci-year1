# dijkstra test

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.visited = False


def connect(node1, node2, weight):
    node1.connections.append({"node": node2, "weight": weight})
    node2.connections.append({"node": node1, "weight": weight})

def get_all_nodes(node):
    '''Return a list of the nodes in the graph of nodes connected to node
    (N.B., the nodes can be indirectly connected as well)'''
    res = []
    q = [node]
    node.visited = True
    while len(q) > 0:
        cur = q.pop(0) # remove q[0] from q and put it in cur
        res.append(cur.name)
        for con in cur.connections:
            if not con["node"].visited:
                q.append(con["node"])
                con["node"].visited = True
    return res

def dijkstra(node):
    pass
