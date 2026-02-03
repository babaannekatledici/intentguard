import networkx as nx

def build_graph(seq):
    G = nx.DiGraph()
    for i in range(len(seq)-1):
        G.add_edge(seq[i], seq[i+1])
    return G
