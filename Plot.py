import networkx as nx
import matplotlib.pyplot as plt

class plot:
    def __init__(self, original_graph,spanning_graph):
        self.original_graph = original_graph
        self.spanning_graph = spanning_graph

    def plot(self):
        plt.figure(figsize=(5, 10))

        # Define the original graph
        G = nx.Graph()
        for node1,node2,weight in self.original_graph:
            # convert digital node to letter
            node1, node2 = chr(node1+65), chr(node2+65)
            G.add_edge(node1, node2, weight=int(weight))

        
        # Graph spanning tree
        T = nx.Graph()
        for node1,node2,weight in self.spanning_graph:
            # convert digital node to letter
            node1, node2 = chr(node1+65), chr(node2+65)
            T.add_edge(node1, node2, weight=int(weight))
        

        # Draw the graph with labels
        pos = nx.spring_layout(G)
        # Draw the original graph
        nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5)
        nx.draw_networkx_nodes(G, pos, node_size=200)
        nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, label_pos=0.4, font_size=10)

        # Draw the minimum spanning tree
        nx.draw_networkx_edges(T, pos, edge_color='red', alpha=1.0, width=2)
        nx.draw_networkx_nodes(T, pos, node_size=200, node_color='red')
        nx.draw_networkx_edge_labels(T, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, label_pos=0.4, font_size=10)
        # Show the plot
        plt.axis('off')
        plt.show()
