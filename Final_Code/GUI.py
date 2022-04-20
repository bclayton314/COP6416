#This is handling for MAC specific OS
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from AStar_Algo import A_Star_Search
from Prim import PrimMST
from adj_matrix import Adj_Matrix


# Displays the initial graph before calculation
def display_initial():
    plt.clf()
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
    g.add_edge(12, 3, 2)
    np_matrix = np.matrix(g.adjMatrix)
    display_graph = nx.from_numpy_matrix(np_matrix)
    pos = nx.spring_layout(display_graph, seed=100)
    nx.draw(display_graph, pos, with_labels=True)
    edge_labels = dict([((n1, n2), d['weight'])
                        for n1, n2, d in display_graph.edges(data=True)])
    nx.draw_networkx_edge_labels(display_graph, pos, edge_labels=edge_labels)
    plt.show()


# Code to format the path through the graph
def display_path(path_data_result):
    plt.clf()
    path_list = []
    length_test_result = len(path_data_result)
    i = 0
    while i < length_test_result - 1:
        next_stop = path_data_result[i + 1]
        path_list.append((path_data_result[i], next_stop))
        i += 1
    return path_list


# Takes input from GUI to calculate Dijkstra'a Algo
def calculate_dijkstra():
    if v.get() == '1':  # min_heap is 1
        A_Star_bool = True
    else:
        A_Star_bool = False
    try:
        results = A_Star_Search(g, int(start_entry.get()), int(stop_entry.get()), A_Star_bool)
    except:
        error_lbl = tk.Label(root, text="***Error.  Please select a whole number from the nodes in the graph.***", font=('Helvetica bold', 12))
        error_lbl.pack()
    display_initial()
    display_path(results)


# Takes input from GUI to calculate Prim's MST
def calculate_display_prim():
    if v2.get() == '1':  # min_heap is 1
        prim_bool = True
    else:
        prim_bool = False
    try:    
        prim_results = PrimMST(g, int(prim_start.get()), prim_bool)
    except:
        error_lbl = tk.Label(root, text="***Error.  Please select a whole number from the nodes in the graph.***", font=('Helvetica bold', 12))
        error_lbl.pack()
    display_initial()
    np_matrix = np.matrix(g.adjMatrix)
    display_graph = nx.from_numpy_matrix(np_matrix)
    display_graph.add_edges_from(prim_results)
    pos = nx.spring_layout(display_graph, seed=100)
    nx.draw_networkx_nodes(display_graph, pos)
    nx.draw_networkx_labels(display_graph, pos)
    nx.draw_networkx_edges(display_graph, pos, edgelist=prim_results, width=2, edge_color="red", arrows=False)
    plt.show()


# Code to actually display paths through the graph
def display_path(path_data_result):
    path_list = []
    length_test_result = len(path_data_result)
    i = 0
    while i < length_test_result - 1:
        next_stop = path_data_result[i + 1]
        path_list.append((path_data_result[i], next_stop))
        i += 1
    np_matrix = np.matrix(g.adjMatrix)
    display_graph = nx.from_numpy_matrix(np_matrix)
    display_graph.add_edges_from(path_list)
    pos = nx.spring_layout(display_graph, seed=100)
    nx.draw_networkx_nodes(display_graph, pos)
    nx.draw_networkx_labels(display_graph, pos)
    nx.draw_networkx_edges(display_graph, pos, edgelist=path_list, width=2, edge_color="red", arrows=False)
    plt.show()


# Takes input from GUI and displays added edge
def add_edge_variables():
    try:
        g.add_edge(int(extra_edge_start.get()), int(extra_edge_stop.get()), int(extra_edge_weight_int.get()))
    except:
        error_lbl = tk.Label(root, text="***Error.  Please select a whole number from the nodes in the graph.***", font=('Helvetica bold', 12))
        error_lbl.pack()
    display_initial()



if __name__ == '__main__':
    # Tkinter code for GUI
    g = Adj_Matrix(13)

    root = tk.Tk()
    greeting = tk.Label(root, text="Shortest Paths and Minimum Spanning Trees", 
                        font=('Helvetica bold', 14), height=4, width=60)
    instructions = tk.Label(root, text="Please enter your Start and Stop Nodes for A* Dijkstra", font=('Helvetica bold', 11))
    results_output = tk.Text(root)

    #Create the buttons to run the functions for A*, Prims, or adding an edge to the graph
    dijkstra_button = tk.Button(root, text="Calculate A* Dijkstra's", command=calculate_dijkstra)
    primMST_button = tk.Button(root, text="Prim's MST", command=calculate_display_prim)
    add_edge_button = tk.Button(root, text="Add Edge", command=add_edge_variables)

    start = tk.Label(root, text="Start") #Create a label for the start entry textbox
    start_entry = tk.Entry(root) 

    stop = tk.Label(root, text="Stop") #Create a label for the stop entry textbox
    stop_entry = tk.Entry(root)

    #Create a label to indicate Prim's calculation
    prims_instruction_lbl = tk.Label(root, text="Or you can plot Prim's MST", font=('Helvetica bold', 11))
    prims_start_lbl = tk.Label(root, text="Prim's Start Node")
    prim_start = tk.Entry(root) #Create entry box for prim's start node entry

    #Create labels and entry boxes for extra edge and weight commands
    extra_edge_lbl = tk.Label(root, text="Or you can add an extra Edge to the Graph", font=('Helvetica bold', 11))

    extra_edge_start_lbl = tk.Label(root, text="Extra Edge Start")
    extra_edge_start = tk.Entry(root)

    extra_edge_stop_lbl = tk.Label(root, text="Extra Edge Stop")
    extra_edge_stop = tk.Entry(root)

    extra_edge_weight = tk.Label(root, text="Edge Weight")
    extra_edge_weight_int = tk.Entry(root)

    #Pack the greeting, instructions, start/stop entry boxes to the GUI window
    greeting.pack()
    instructions.pack()
    start.pack()
    start_entry.pack()
    stop.pack()
    stop_entry.pack()

    # Dijkstra's radio buttons - Initialize the variable to 1 as the default selection
    # Set a value for min_heap and linkedlist, then pass that variable into the radiobutton 
    v = tk.StringVar(root, "1")
    dijkstra_values = {"min_heap": "1",
                    "LinkedList": "2"}

    for (text, value) in dijkstra_values.items():
        tk.Radiobutton(root, text=text, variable=v,
                    value=value).pack(side=tk.TOP, ipady=5)

    dijkstra_button.pack() #Pack the button to the window

    #Create some spacing for better visibility
    empty_line_lbl1 = tk.Label(root, text="")
    empty_line_lbl1.pack()
    prims_instruction_lbl.pack()

    # Prim's radio buttons - Initialize the variable to 1 as the default selection
    # Set a value for min_heap and linkedlist, then pass that variable into the radiobutton
    v2 = tk.StringVar(root, "1")
    prim_values = {"min_heap": "1",
                "LinkedList": "2"}

    for (text, value) in prim_values.items():
        tk.Radiobutton(root, text=text, variable=v2,
                    value=value).pack(side=tk.TOP, ipady=5)

    prims_start_lbl.pack()
    prim_start.pack()
    primMST_button.pack()
    empty_line_lbl2 = tk.Label(root, text="")
    empty_line_lbl2.pack()
    extra_edge_lbl.pack()
    extra_edge_start_lbl.pack()
    extra_edge_start.pack()
    extra_edge_stop_lbl.pack()
    extra_edge_stop.pack()
    extra_edge_weight.pack()
    extra_edge_weight_int.pack()
    add_edge_button.pack()

    display_initial() #Create the initial graph to show the user

    root.mainloop() #Listens for the button commands to interact with the user







