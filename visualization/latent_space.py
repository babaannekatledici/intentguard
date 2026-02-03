from sklearn.decomposition import PCA
import numpy as np

def plot_latent(embeddings):
    embeddings = np.array(embeddings)

    if len(embeddings) < 3:
        print("⚠️ Not enough points for PCA, skipping latent plot")
        return

    if np.isnan(embeddings).any() or np.isinf(embeddings).any():
        print("⚠️ Invalid values in embeddings, skipping PCA")
        return

    pca = PCA(n_components=2)
    X = pca.fit_transform(embeddings)

    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(X[:, 0], X[:, 1], marker="o")
    plt.title("Latent Intent Trajectory")
    plt.show(block=False)
