
class Adj_Matrix(object):


    # Define the matrix
    def __init__(self, numNodes):
        self.adjMatrix = []
        for node in range(numNodes):
            self.adjMatrix.append([0 for node in range(numNodes)])
        self.size = numNodes


    # Add an edge to the graph
    def add_edge(self, node1, node2, weight):
        if node1 == node2:
            print("Cannot add edge to/from same node")
        self.adjMatrix[node1][node2] = weight
        self.adjMatrix[node2][node1] = weight


    # Remove an edge from the graph
    def remove_edge(self, node1, node2):
        if self.adjMatrix[node1][node2] == 0:
            print("No edge exists to/from same node")
            return
        self.adjMatrix[node1][node2] = 0
        self.adjMatrix[node2][node1] = 0

    def __len__(self):
        return self.size

    # Iterate through and print the values in the matrix
    def print_adj_matrix(self):
        for node in self.adjMatrix:
            for val in node:
                print(val, end = " ")
            print()
    def neighbors(self, Node):
        return self.adjMatrix[Node.id]



