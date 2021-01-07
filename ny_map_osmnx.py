import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors



place = 'New york city,New York, USA'
G = ox.graph_from_place(place, network_type='drive')

# convert your MultiDiGraph to an undirected MultiGraph
#M = ox.get_undirected(G)

# convert your MultiDiGraph to a DiGraph without parallel edges
#D = ox.get_digraph(G)

#fig, ax = ox.plot_graph(G,node_size=0, edge_linewidth=0.5)