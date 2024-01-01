import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

# Get the input file
code = {}

with open('input') as f:
    loop = f.readline().rstrip()

    line = f.readline()
    line = f.readline().rstrip()

    while line != '':
        parsing = line.split('=')
        parsing[1] = parsing[1].replace(')', '')
        parsing[1] = parsing[1].replace('(', '')
        parsing[1] = parsing[1].replace(' ', '')
        code[parsing[0].strip()] = parsing[1].split(',')
        line = f.readline().rstrip()


# Create the graph
my_graph = nx.DiGraph()

# Adding nodes
#my_graph.add_nodes_from(code.keys())

for node in code.keys():

    if node[-1] == 'A':
        color = 'green'
    elif node[-1] == 'Z':
        color = 'red'
    else:
        color = 'blue'
    my_graph.add_node(node, color = color, size = 0.1)        
    my_graph.add_edge(node, code[node][0], weight = 'purple')
    my_graph.add_edge(node, code[node][1], weight = 'orange')







    
# Plot the graph
plt.figure(figsize = (50, 50))
pos = nx.nx_agraph.graphviz_layout(my_graph)
nodes = nx.draw_networkx_nodes(
    my_graph, pos, nodelist = [node for node in my_graph.nodes],
    node_color = [my_graph.nodes[node]['color'] for node in my_graph.nodes])
edges = nx.draw_networkx_edges(
    my_graph, pos,
    edgelist = [edge for edge in my_graph.edges],
    edge_color = [my_graph.edges[edge]['weight'] for edge in my_graph.edges])

pc = mpl.collections.PatchCollection(edges)



plt.savefig('route_graphs.png', dpi = 100)
