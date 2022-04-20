from msilib.schema import Class
from re import X


class Graph_Adjacency:
    def __init__(self, x):
        self.x = x

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Location:
    def __init__(self, loc):
        self.loc = loc