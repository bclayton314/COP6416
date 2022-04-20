
from math import sqrt
import numpy as np
import networkx as nx
from LinkedList_Prio_Queue import LinkedListPriorityQueue, PriorityQueueNode
from adj_matrix import Adj_Matrix
from min_heap import min_heap


node = PriorityQueueNode(7, 1)
g = Adj_Matrix(13)

g.add_edge(0, 1, 7)
g.add_edge(0, 2, 2)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 3)
g.add_edge(1, 4, 4)
g.add_edge(2, 8, 1)
g.add_edge(2, 4, 4)
g.add_edge(4, 6, 5)
g.add_edge(8, 6, 3)
g.add_edge(8, 7, 2)
g.add_edge(7, 5, 2)
g.add_edge(5, 11, 5)
g.add_edge(11, 9, 4)
g.add_edge(11, 10, 4)
g.add_edge(9, 10, 6)
g.add_edge(9, 12, 4)
g.add_edge(10, 12, 4)
g.add_edge(12, 3, 2)
hlist_test = []

np_matrix = np.matrix(g.adjMatrix)
display_graph = nx.from_numpy_matrix(np_matrix)

pos = nx.spring_layout(display_graph, seed=100)
nx.draw(display_graph, pos, with_labels=True)

# Creates list of Euclidean distance to end node for heuristic
def create_hlist(start, stop):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    hlist2 = []
    for (j, (x, y)) in pos.items():
        if j == stop:
            x2 = abs(x)
            y2 = abs(y)
            break
    for (i, (x, y)) in pos.items():
        x1 = abs(x)
        y1 = abs(y)
        hlist2.append(sqrt((y2 - y1)**2 + (x2 - x1)**2))

    return hlist2

#Function to provide reconstruction of the path to pass to GUI
#inputs are NodeCameFromMap and the last node discovered (end node)
#output is a list of the nodes in the order they were traversed
def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        if current != None:
            total_path.insert(0, current)
    return total_path


#A* Search algorithm function that returns the shortest path from the start to the end node using Euclidean distance as heuristic
#inputs are adjacency matrix graph, starting node, ending node, and boolean to determine what data structure to use for priority queue
#output a list of the nodes on the path to the shortest path using A*
def A_Star_Search(graph, start, end, min_heap_boolean):
    #Data structure initialization based on inputed boolean
    if (min_heap_boolean == True):
        PrioQueue = min_heap(30)  
    else:
        PrioQueue = LinkedListPriorityQueue()
    PrioQueue.push(PriorityQueueNode(0, start)) #Push starting node
    #Initialize of the three Dictionaries (Maps) to be used for storing values of current nodes and provide easy lookup of the most optimal values for compariion
    Node_Came_From = {}
    G_Score = {}
    F_Score = {}
    Node_Came_From[start] = None
    G_Score[start] = 0 #Starting node G Score set to 0 because no cost to get to starting node
    hlist_test = create_hlist(start, end) #Creates a list of the h portion of the algorithm that provides the euclidean distance 
    F_Score[start] = hlist_test[0] #Fscore is G score + h score so set to just the distance to the end node.

    #Loop to move through the Priority queue
    while not PrioQueue.isEmpty():
        neighborCount = 0 #Variable to support iteration through the neighbors of the current node and also keeps track of each nodes unique id
        Current_Node = PrioQueue.pop() #Removing highest priority item from the queue and setting to current node
        #If that node is the end we break out of loop
        if Current_Node.id == end:
            break
        #Loop to iterate through the neighbors of the current node
        for weight in graph.neighbors(Current_Node):
            #If statement to ignore all values that are zero (No edge is present)
            if weight > 0:
                temp_Cost = G_Score[Current_Node.id] + weight #statment grabs the current node G score and adds the neighbor's cost
                #If that neighbor is not currently in the G score map meaning we havent seen that node before or that new calculated cost 
                #is a lower path then what is currently in the map
                if neighborCount not in G_Score or temp_Cost < G_Score[neighborCount]:
                    Node_Came_From[neighborCount] = Current_Node.id #update node came from map to keep track of the best path the node found and to faciliate reconstruction of path
                    G_Score[neighborCount] = temp_Cost #Sets G score value as the best value for that node
                    F_Score[neighborCount] = temp_Cost + hlist_test[neighborCount] ##Sets F score value as the best value for that node
                    PrioQueue.push(PriorityQueueNode(F_Score[neighborCount], neighborCount)) #Pushes that node onto priority queue 
            neighborCount += 1

    results = reconstruct_path(Node_Came_From, Current_Node.id)
    return results





