import numpy as np
import networkx as nx

def graph_features(G):
    return np.array([
        G.number_of_nodes(),
        G.number_of_edges(),
        nx.density(G)
    ])
