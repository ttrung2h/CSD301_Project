
class InputData:
    
    @classmethod
    def input_number_nodes(cls):
        while True:
            try:
                number_nodes = int(input("Enter the number of nodes: "))
                if number_nodes < 1 or number_nodes > 26:
                    print("Number of nodes must be in range 1-26")
                    continue
                return number_nodes
            except:
                print("Node must be a number")
    
    @classmethod
    def input_node(cls, message="Enter the node: ",number_nodes= 0):
        while True:
            node = input(message).upper()

            # check node out range
            if node not in [chr(i) for i in range(65,65+number_nodes)]:
                print(f"Node must be in range A - {chr(65+number_nodes-1)}")
                continue
            return node
    
    @classmethod
    def input_weight(cls):
        while True:
            try:
                weight = int(input("Enter the weight: "))
                return weight
            except:
                print("Weight must be a integer number")
    @classmethod
    def input_yes_no(cls, message="Do you want to continue? (Y/N)"):
        while True:
            answer = input(message).upper()
            if answer not in ["Y", "N"]:
                print("Answer must be Y or N")
                continue
            return answer