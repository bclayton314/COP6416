
from LinkedList_Prio_Queue import LinkedListPriorityQueue, PriorityQueueNode
from min_heap import min_heap

#Function to calculate the Prims Minimal Spanning tree for a graph
#Inputs are the adjancency matrix repersentation of the graph, starting node, and the data structure boolean
#Outputs List of tuples of the nodes the edges connect to
def PrimMST(graph, start, min_heap_boolean):
    prim_results = []
    breakLoop = False
    #data structure determination
    if(min_heap_boolean == True):
        PrioQueue = min_heap(30) #30 is place holder for number of nodes
    else:
        PrioQueue = LinkedListPriorityQueue()
    PrioQueue.push(PriorityQueueNode(0, start))
    #Maps and counter initialization to provide access to stored data
    node_Visited_Counter = 0
    node_Visited = {}
    node_From = {}
    map_Weights = {}
    #Loop to move through the Priority queue
    while not PrioQueue.isEmpty():
        neighborCount = 0
        Current_Node = PrioQueue.pop() #Remove and visit current node from the priority queue
        node_Visited_Counter += 1
        #If all nodes visisted break out of loop
        if node_Visited_Counter == 14:
            break
        #Loop if the current popped off node has been visited
        while Current_Node.id in node_Visited:
            Current_Node = PrioQueue.pop() #Reterive the next node with the highest priority
        if Current_Node.id != start:
            prim_results.append((int(node_From[Current_Node.id]), int(Current_Node.id))) #appends the tuple to the result
        node_Visited[Current_Node.id] = True #Marks node as visited
        #Loop through neighbors
        for weight in graph.neighbors(Current_Node):
            if weight > 0:
                #If node hasnt been seen or current weight is better than stored wait update Maps and push node
                if neighborCount not in map_Weights or weight < map_Weights[neighborCount]:
                    node_From[neighborCount] = Current_Node.id
                    map_Weights[neighborCount] = weight
                    PrioQueue.push(PriorityQueueNode(weight,neighborCount))
            neighborCount += 1

    return prim_results









