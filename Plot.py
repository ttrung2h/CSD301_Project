import networkx as nx
import matplotlib.pyplot as plt
import tqdm
class plot:
    def __init__(self,num_of_nodes, original_graph,spanning_graph):
        self.num_of_nodes = num_of_nodes
        self.original_graph = original_graph
        self.spanning_graph = spanning_graph

    def plot(self):
        
        # Define the original graph
        G = nx.Graph()
        for node1,node2,weight in self.original_graph:
            # convert digital node to letter
            node1, node2 = chr(node1+65), chr(node2+65)
            G.add_edge(node1, node2, weight=int(weight))

        
        # Draw the graph with labels
        pos = nx.spring_layout(G)
        
        # Graph spanning tree
        T = nx.Graph()
        for i,(node1,node2,weight) in enumerate(self.spanning_graph):
            fig = plt.figure(figsize=(10,12))
            # Draw the original graph
            nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5)
            nx.draw_networkx_nodes(G, pos, node_size=1000)
            nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, label_pos=0.4, font_size=10)
            # convert digital node to letter
            node1, node2 = chr(node1+65), chr(node2+65)
            
            # Draw the minimum spanning tree
            T.add_edge(node1, node2, weight=int(weight))
            nx.draw_networkx_edges(T, pos, edge_color='red', alpha=1.0, width=2)
            nx.draw_networkx_nodes(T, pos, node_size=1000, node_color='red')
            nx.draw_networkx_edge_labels(T, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, label_pos=0.4, font_size=10)
            plt.savefig(fname = f'result/Step_{i}.png')
        print("All image saved in result folder")
