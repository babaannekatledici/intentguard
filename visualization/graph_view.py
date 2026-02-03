import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, title="Behavior Graph"):
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        node_size=50,
        with_labels=False,
        edge_color="gray"
    )

    plt.title(title)
    plt.show(block=False)

