from GraphAlgorithms.py import *

graph = Graph()

while graph.size < 5:
    graph.add_node()


eighty_percent_of_edges = 0.8 * graph.number_of_edges
while graph.number_of_edges > eighty_percent_of_edges:
    graph.del_random_edge()

graph.print_nodes()

starting_node = int(input("\nChoose the starting city: "))
s_node = int(input("The start city (bidirectional search): "))
e_node = int(input("The end city (bidirectional search): "))


if graph.is_closed_tour():
    print("\nBFS:")
    graph.bfs(starting_node)
    print("\nDFS:")
    graph.dfs(starting_node)
    print("\nMinimum spanning tree:")
    graph.minimum_spanning_tree(starting_node)
    print("\nGreedy search:")
    graph.greedy_search(starting_node)
else:
    print("\nRoute is impossible!.")
if graph.is_route_possible(s_node, e_node):
    print("\nBidirectional search:")
    graph.bidirectional_search(s_node, e_node)
else:
    print("Unable to get a route using bidirectional search.")
