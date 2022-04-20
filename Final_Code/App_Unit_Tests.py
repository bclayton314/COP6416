from AStar_Algo import *
from Prim import *
import unittest

class TestAlgo(unittest.TestCase):
    def test_min_heap(self):
        minHeap = min_heap(15)
        minHeap.push(PriorityQueueNode(5,'A'))
        self.assertEqual(minHeap.Heap[1].id, 'A')
        minHeap.push(PriorityQueueNode(3, 'B'))
        minHeap.push(PriorityQueueNode(17, 'C'))
        minHeap.push(PriorityQueueNode(10, 'D'))
        minHeap.push(PriorityQueueNode(84, 'E'))
        minHeap.push(PriorityQueueNode(19, 'F'))
        minHeap.push(PriorityQueueNode(6, 'G'))
        minHeap.push(PriorityQueueNode(22, 'H'))
        minHeap.push(PriorityQueueNode(9, 'I'))
        testNode = minHeap.pop()
        self.assertEqual(testNode.id,'B')
        for count in range(7):
            minHeap.pop()
        testNode = minHeap.pop()
        self.assertEqual(testNode.id,'E')
    
    def test_LL_prio_queue(self):
        pq = LinkedListPriorityQueue()
        pq.push(PriorityQueueNode(5,'A'))
        self.assertEqual(pq.front.id, 'A')
        pq.push(PriorityQueueNode(3, 'B'))
        pq.push(PriorityQueueNode(17, 'C'))
        pq.push(PriorityQueueNode(10, 'D'))
        pq.push(PriorityQueueNode(84, 'E'))
        pq.push(PriorityQueueNode(19, 'F'))
        pq.push(PriorityQueueNode(6, 'G'))
        pq.push(PriorityQueueNode(22, 'H'))
        pq.push(PriorityQueueNode(9, 'I'))
        testNode = pq.pop()
        self.assertEqual(testNode.id,'B')
        for count in range(7):
            pq.pop()
        testNode = pq.pop()
        self.assertEqual(testNode.id,'E')

    def testGraph(self):
        g = Adj_Matrix(4)
        g.add_edge(0,1,7)
        self.assertEqual(g.adjMatrix[0][1], 7)
        self.assertEqual(g.adjMatrix[1][0], 7)

    def test_prim(self):
        g = Adj_Matrix(13)
        path_min_heap = [(0, 2), (2, 8), (8, 7), (7, 5), (8, 6), (0, 3), (3, 12), (2, 1), (12, 9), (2, 4), (9, 11), (12, 10)]
        path_LL = [(0, 2), (2, 8), (8, 7), (7, 5), (8, 6), (2, 1), (0, 3), (3, 12), (12, 10), (12, 9), (10, 11), (2, 4)]
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
        self.assertEqual(PrimMST(g,0,True), path_min_heap)
        self.assertEqual(PrimMST(g,0,False), path_LL)

    def testAStar(self):
        path = [0, 2, 8, 7]
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
        self.assertEqual(A_Star_Search(g,0,7,True), path)
        self.assertEqual(A_Star_Search(g,0,7,False), path)

if __name__ == '__main__':
    unittest.main()