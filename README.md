# IntentGuard 🔐
**Online Intent Drift Detection using Linux Syscalls, Graphs, and Self-Supervised Learning**

---

## 🚀 Overview

IntentGuard is a security research project that detects **behavioral intent drift** in Linux systems using **raw syscall data**.
Instead of relying on signatures or labeled attack datasets, IntentGuard learns **normal behavior intent** and raises alerts when system behavior **semantically changes over time**.

This makes it suitable for detecting:
- Zero-day attacks
- Stealthy, slow attacks
- Insider threats
- Living-off-the-land attacks

---

## 🧠 Core Idea

> **Intent matters more than individual actions.**

Rather than detecting *what command* was run, IntentGuard models:
- **How behavior evolves**
- **How syscall patterns change structurally**
- **When intent drifts beyond a safe threshold**

---

## 🏗️ Architecture

Linux Syscalls
↓
Parsing & Normalization
↓
Sliding Windows
↓
Sequence Encoder (LSTM)
↓
Graph Construction (Syscall Transitions)
↓
Graph + Sequence Fusion
↓
Intent Embeddings
↓
Online Drift Detection
↓
Explainability & Visualization

---

## 📁 Project Structure

intentguard/
│
├── data/
│ └── raw/
│ ├── normal_syscalls.log
│ └── attack_syscalls.log
│
├── ingestion/
│ ├── audit_parser.py # Parses syscall logs
│ └── normalize.py # Converts syscalls to numeric IDs
│
├── simulation/
│ └── attack_simulator.py # Injects attack-like behavior
│
├── graph/
│ ├── build_graph.py # Builds syscall transition graphs
│ ├── graph_features.py # Extracts graph features
│ └── graph_embeddings.py # Embeds graph features
│
├── model/
│ ├── intent_encoder.py # LSTM-based intent encoder
│ └── train.py # Self-supervised training
│
├── detection/
│ └── online_detector.py # Online intent drift detection
│
├── visualization/
│ ├── latent_space.py # Latent intent trajectory
│ ├── trajectory_plot.py # Intent similarity over time
│ ├── graph_view.py # Behavior graph snapshot
│ └── comparison_plot.py # Normal vs Attack comparison
│
├── run_pipeline.py # End-to-end pipeline
├── requirements.txt
└── README.md

---

## 📊 Visual Outputs

IntentGuard produces **four explainable plots**:

1. **Behavior Graph Snapshot**
   Shows structural syscall changes at the drift point.

2. **Latent Intent Trajectory**
   2D projection of intent embeddings over time.

3. **Intent Drift Over Time**
   Cosine similarity decay with drift threshold.

4. **Normal vs Attack Comparison**
   Shows separation between benign and attack intent clusters.

---

## ⚙️ Setup Instructions

### 1️⃣ Create Conda Environment
conda create -n intentguard python=3.10
conda activate intentguard

### 2️⃣ Install Dependencies
pip install -r requirements.txt

📥 Collecting Syscall Logs (Ubuntu)
Normal behavior
strace -e trace=openat,read,write,execve -o normal_syscalls.log bash

Run normal commands, then:
exit

Attack-like behavior (safe)
strace -e trace=openat,read,write,execve -o attack_syscalls.log bash

Run reconnaissance-style commands, then:
exit

Place logs in:
data/raw/

▶️ Running the Pipeline
python run_pipeline.py

Expected output:
Drift alert in terminal
Multiple visualization windows

👨‍💻 Author

Akshat Pal
