import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def compare_intent(normal_embeddings, attack_embeddings):
    """
    Plots normal vs attack intent trajectories in the same latent space
    """
    pca = PCA(n_components=2)

    all_embeddings = np.vstack([normal_embeddings, attack_embeddings])
    reduced = pca.fit_transform(all_embeddings)

    n = len(normal_embeddings)
    normal_2d = reduced[:n]
    attack_2d = reduced[n:]

    plt.figure(figsize=(7, 5))
    plt.plot(normal_2d[:,0], normal_2d[:,1],
             marker="o", label="Normal Behavior")
    plt.plot(attack_2d[:,0], attack_2d[:,1],
             marker="x", label="Attack Behavior")

    plt.title("Normal vs Attack Intent Trajectories")
    plt.xlabel("Latent Dimension 1")
    plt.ylabel("Latent Dimension 2")
    plt.legend()
    plt.grid(True)
    plt.show()
