class Valid:
    @classmethod 
    def is_connected(cls,matrix):
        """
        Returns True if the matrix represents a connected graph, False otherwise.
        """
        # Initialize visited set and stack for DFS
        visited = set()
        stack = [0]  # Start DFS from node 0

        # Perform DFS until stack is empty
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                # Add unvisited neighbors to stack
                for neighbor, connected in enumerate(matrix[node]):
                    if connected and neighbor not in visited:
                        stack.append(neighbor)

        # If all nodes are visited, graph is connected
        return len(visited) == len(matrix)

    @classmethod
    def check_yes_no(cls,answer):
        if answer == "Y":
            return True
        else:
            return False