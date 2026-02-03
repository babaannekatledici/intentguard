from .trajectory import update_trajectory
from .drift_detector import detect_drift

def online_step(traj, emb, index):
    traj.append(emb)
    if len(traj) < 2:
        return traj, False, None, None

    import numpy as np
    sim = np.dot(traj[-2], traj[-1]) / (
        np.linalg.norm(traj[-2]) * np.linalg.norm(traj[-1])
    )

    alert = sim < 0.85
    return traj, alert, sim, index

