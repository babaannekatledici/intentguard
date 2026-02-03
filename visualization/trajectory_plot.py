import matplotlib.pyplot as plt

def plot_similarity(similarities, threshold):
    """
    similarities: list of cosine similarity scores over time
    threshold: drift threshold
    """
    plt.figure(figsize=(8, 4))
    plt.plot(similarities, label="Intent Similarity")
    plt.axhline(threshold, color="red", linestyle="--", label="Drift Threshold")
    plt.xlabel("Time Window")
    plt.ylabel("Cosine Similarity")
    plt.title("Intent Drift Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()
