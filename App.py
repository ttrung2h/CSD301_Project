from Graph import Graph
from Plot import plot
from InputData import InputData
from Valid import Valid
if __name__ == "__main__":
    number_of_nodes = InputData.input_number_nodes()
    
    # create matrix 2 dimension have length = number_of_nodes
    matrix = [[0 for i in range(number_of_nodes)] for j in range(number_of_nodes)]
    G = Graph(number_of_nodes)
    
    # loop input edge
    while True:
        #input node1
        node1 = InputData.input_node("Enter the node1: ", number_of_nodes)
        node1 = ord(node1) - 65
        
        #input node2
        node2 = InputData.input_node("Enter the node2: ", number_of_nodes)
        node2 = ord(node2) - 65
        
        #input weight
        weight = InputData.input_weight()
        
        # Check edge already exists
        if matrix[node1][node2] != 0 and matrix[node2][node1] != 0:
            answer = InputData.input_yes_no("Edge already exists. Do you want to replace? (Y/N): ")
            if not Valid.check_yes_no(answer):
                continue
        
        matrix[node1][node2],matrix[node2][node1] = weight,weight
        G.add_edge(node1, node2, weight)
        
        # Check graph fully connected
        if Valid.is_connected(matrix):
            answer = InputData.input_yes_no("Graph is connected. Do you want to continue? (Y/N): ")
            if not Valid.check_yes_no(answer):
                break
        
        
    
    # show matrix
    print(matrix)
    original_graph = G.get_orignal_graph()
    spanning_graph = G.kruskals_mst()
    print(original_graph)
    print(spanning_graph)
    show_graph = plot(original_graph, spanning_graph)
    show_graph.plot()
    
