import networkx as nx
import osmnx as ox
import requests
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as colors

df = pd.read_csv('data/edges_of_nyc.csv')
####Create a class path who will define our function for the project.
### Our class should take as parameter the origin and destination at least

### Our first function should check the type of destination  and origin is it coordinate or string ? then dispatch to the right function.
### second function and third should check if the given origin/destination are in a df that i will create with all street of NYC if not return error
### else if it exist we should check for the safest path ( maybe call another function to keep it short)
## Your should return the plot of the path for the template(safest_path.html) it's already waiting for the response
place = 'New york city,New York, USA'
G = ox.graph_from_place(place, network_type='drive')


class NYMapOSMnx:
    """This class will create the edge graph of New York and will find the shortest and least dangerous route from a to b"""

    def creat_graph(self, place: str):
        """This function will create the graph of New York and return it"""
        place = 'New york city,New York, USA'
        G = ox.graph_from_place(place, network_type='drive')
        return G

   def getSafest(self, origin,destination):
        route = ox.shortest_path(G, origin, destination, weight='length')
        #fig, ax = ox.plot_graph_route(G, route, route_color='y', route_linewidth=6, node_size=0)
        #fig, ax = ox.plot_graph(G,node_size=0, edge_linewidth=0.5)

    def isPresent(self, origin,destination):
        if origin == df.name and destination == df.name :
            print('coucou')
            return True
        elif origin != df.name:
            print('coucou2')
            return 'Wrong origin'
        elif destination != df.name:
            print('coucou3')
            return 'Wrong destination'
    #fig, ax = ox.plot_graph_route(G, route, route_color='y', route_linewidth=6, node_size=0)

    # convert your MultiDiGraph to an undirected MultiGraph
    #M = ox.get_undirected(G)
    # convert your MultiDiGraph to a DiGraph without parallel edges
    #D = ox.get_digraph(G)
    #fig, ax = ox.plot_graph(G,node_size=0, edge_linewidth=0.5)

place = 'New york city,New York, USA'
G = ox.graph_from_place(place, network_type='drive')
print(G.head(100))
