import numpy as np

def embed_graph(features):
    n = np.linalg.norm(features)
    return features if n == 0 else features / n
