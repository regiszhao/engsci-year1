class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.visited = False

    def __lt__(self, node2):
        return True

def connect(node1, node2, weight):
    node1.connections.append({"node": node2, "weight": weight})
    node2.connections.append({"node": node1, "weight": weight})



def dijsktra_pq(node):
    d = {}
    pq = [(0, node)]
    while len(pq) > 0:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_node.name in d:
            continue
        d[cur_node.name] = cur_dist
        for con in cur_node.connections:
            dist = con["weight"] + cur_dist
            node = con["node"]
            heapq.heappush(pq, (dist, node))
    return d



if __name__ == '__main__':
    TO = Node("TO")
    NYC = Node("NYC")
    DC = Node("DC")
    CDMX = Node("CDMX")
    SF = Node("SF")

    connect(TO, NYC, 3)
    connect(TO, SF, 6)
    connect(TO, CDMX, 7)
    connect(NYC, DC, 2)
    connect(SF, DC, 5)

    dijsktra_pq(TO)