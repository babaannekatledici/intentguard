import numpy as np

def cosine(a, b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

def detect_drift(traj, threshold=0.85):
    if len(traj) < 2:
        return False, None
    sim = cosine(traj[-2], traj[-1])
    return sim < threshold, sim
