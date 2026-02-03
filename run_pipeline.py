import torch
import numpy as np
import matplotlib.pyplot as plt
from ingestion.audit_parser import parse_syscalls
from ingestion.normalize import normalize
from simulation.attack_simulator import inject_attack

from graph.build_graph import build_graph
from graph.graph_features import graph_features
from graph.graph_embeddings import embed_graph

from model.train import train
from detection.online_detector import online_step

from visualization.latent_space import plot_latent
from visualization.graph_view import draw_graph
from visualization.trajectory_plot import plot_similarity
from visualization.comparison_plot import compare_intent

# -----------------------------
# Load data
# -----------------------------
normal = parse_syscalls("data/raw/normal_syscalls.log")
attack = parse_syscalls("data/raw/attack_syscalls.log")

events = inject_attack(normal, attack)
encoded, vocab = normalize(events)

# -----------------------------
# Build windows
# -----------------------------
WINDOW = 6
sequences = [encoded[i:i+WINDOW] for i in range(len(encoded)-WINDOW)]

graphs = []
for seq in sequences:
    G = build_graph(seq)
    feats = graph_features(G)
    graphs.append(embed_graph(feats))

# -----------------------------
# Train encoder + fusion
# -----------------------------
enc, fusion = train(sequences, graphs, len(vocab))

# -----------------------------
# Online detection
# -----------------------------
trajectory = []
embeddings = []
similarities = []

normal_embeddings = []
attack_embeddings = []

# Assume attack injected AFTER normal
normal_cutoff = len(normal)
first_drift_shown = False

for idx, (seq, g) in enumerate(zip(sequences, graphs)):
    x = torch.tensor(seq).unsqueeze(0)
    g_tensor = torch.tensor(g).unsqueeze(0).float()

    with torch.no_grad():
        seq_emb = enc(x)
        fused = fusion(seq_emb, g_tensor).numpy()[0]

    trajectory, alert, score, drift_index = online_step(
        trajectory, fused, idx
    )

    embeddings.append(fused)

    if score is not None:
        similarities.append(score)

    # Split normal vs attack embeddings
    if idx < normal_cutoff:
        normal_embeddings.append(fused)
    else:
        attack_embeddings.append(fused)

    # Explain drift immediately
    if alert and not first_drift_shown:
        print(f"🚨 Drift detected at index {drift_index}")
        G = build_graph(seq)
        draw_graph(G, title=f"Behavior Graph at Drift Index {drift_index}")
        first_drift_shown = True

# -----------------------------
# FINAL PLOTS (THIS WAS MISSING)
# -----------------------------
print("📊 Generating final plots...")

plot_latent(np.array(embeddings))
plot_similarity(similarities, threshold=0.85)

if len(normal_embeddings) > 1 and len(attack_embeddings) > 1:
    compare_intent(
        np.array(normal_embeddings),
        np.array(attack_embeddings)
    )
plt.show()
