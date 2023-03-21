class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []
   
    def get_orignal_graph(self):
        return self.m_graph   
    
    
    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1, node2, weight])
    
    # Finds the root node of a subtree containing node `i`
    def find_subtree(self, parent, node):
        if parent[node] == node:
            return node
        return self.find_subtree(parent, parent[node])

    
    # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, rank, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskals_mst(self):
        # Resulting tree
        result = []
        
        # Iterator
        i = 0
        # Number of edges in MST
        e = 0

        # Sort edges by their weight
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
        
        # Auxiliary arrays
        parent = []
        rank = []

        # Initialize `parent` and `rank` arrays
        for node in range(self.m_num_of_nodes):
            parent.append(node)
            rank.append(0)

        # Important property of MSTs
        # number of egdes in a MST is 
        # equal to (m_num_of_nodes - 1)
        while e < (self.m_num_of_nodes - 1):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.m_graph[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)

            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, rank, x, y)
        print(parent)
        print(rank)
        return result
        