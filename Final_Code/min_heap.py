# Min Heap Function

import sys
from LinkedList_Prio_Queue import PriorityQueueNode


class min_heap:

    def __init__(self, max):
        self.max = max
        self.size = 0
        self.Heap = [0] * (self.max + 1)
        self.Heap[0] = PriorityQueueNode(-1 * sys.maxsize, 0)
        self.FRONT = 1

    # Find the parent node of the current node
    def parent(self, node_index):
        return node_index // 2

    # Find the left child of the current node
    def leftChild(self, node_index):
        return 2 * node_index

    # Find the right child of the current node
    def rightChild(self, node_index):
        return (2 * node_index) + 1

    # Find the boolean fscore of if the node has no children (leaf node)
    def leaf(self, node_index):
        return node_index * 2 > self.size

    # Swap two different nodes
    def swap(self, first_node, second_node):
        self.Heap[first_node], self.Heap[second_node] = self.Heap[second_node], self.Heap[first_node]

    # Function to heapify
    def heapify(self, node_index):

        # If the node is a not a leaf node and is also greater than its's children 
        # then we have to swap becasue the minimum should be at the top of the heap
        if not self.leaf(node_index):
            if (self.Heap[node_index].fscore > self.Heap[self.leftChild(node_index)].fscore or
                    self.Heap[node_index].fscore > self.Heap[self.rightChild(node_index)].fscore):

                # Swap with the left child if the left child is the one less than the parent 
                # and heapify the left child
                if self.Heap[self.leftChild(node_index)].fscore < self.Heap[self.rightChild(node_index)].fscore:
                    self.swap(node_index, self.leftChild(node_index))
                    self.heapify(self.leftChild(node_index))

                # Swap with the right child if the right child is the one less than the parent
                # and heapify the right child (check its children isn't greater than it)
                else:
                    self.swap(node_index, self.rightChild(node_index))
                    self.heapify(self.rightChild(node_index))

    # Function to push a node into the heap
    def push(self, Node):
        if self.size >= self.max:
            return

        if self.isEmpty() == True:
            self.front = Node
            return 1
        else:
            self.size += 1
            self.Heap[self.size] = Node

            current = self.size

            while (self.Heap[current]).fscore < (self.Heap[self.parent(current)]).fscore:
                self.swap(current, self.parent(current))
                current = self.parent(current)

    # For testing purposes -- function to print the contents to verify it is working properly
    def PrintHeap(self):
        for i in range(1, (self.size // 2) + 1):
            print(" Parent Node: " + str(self.Heap[i].fscore) + " Left Child Node: " +
                  str(self.Heap[2 * i].fscore) + " Right Child Node: " +
                  str(self.Heap[2 * i + 1].fscore))

    # Build the minHeap by calling heapify on every node
    def minHeap(self):

        for node in range(self.size // 2, 0, -1):
            self.heapify(node)

    # Function to remove and return the minimum element from the heap
    def pop(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1

        self.heapify(self.FRONT)
        return popped

    def isEmpty(self):
        return True if self.Heap[self.FRONT] == None else False