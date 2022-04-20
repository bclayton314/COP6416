import sys
#Class definition of Priority Queue Node for both data structures
class PriorityQueueNode:

    #Constructor for Priority Queue Node
    def __init__(self, fscore, id):
        self.next = None
        self.id = id
        self.fscore = fscore

#Class definition of Priority Queue using a linked list implementation
class LinkedListPriorityQueue:
    #Constructor for Priority Queue
    def __init__(self):
        self.front = None

    #Class Method to determine if queue is empty
    #inputs nothing
    #outputs boolean if empty (True) or populated (False)
    def isEmpty(self):

        return True if self.front == None else False

    #Class Method add on to the queue
    #inputs Priority queue node 
    #updates queue
    def push(self, Prio_Node):
        #If empty add to front
        if self.isEmpty() == True:
            self.front = Prio_Node
            return 1
        #Else check if fscore of node should place in the front of the queue or loop through the queue and find the proper place and insert and repair pointers
        else:
            if self.front.fscore > Prio_Node.fscore:
                Prio_Node.next = self.front
                self.front = Prio_Node
                return 1

            else:
                tempNode = self.front

                while tempNode.next:
                    if Prio_Node.fscore <= tempNode.next.fscore:
                        break

                    tempNode = tempNode.next
                Prio_Node.next = tempNode.next
                tempNode.next = Prio_Node
                return 1
    #Class Method add on to the queue
    #input nothing
    #output Priority queue node at the front of the queue
    def pop(self):
        #If empty return nothing
        if self.isEmpty() == True:
            return
        #Else remove node from the front and repair front pointer the the next node in the queue
        else:
            tempNode = self.front
            self.front = self.front.next
            return tempNode