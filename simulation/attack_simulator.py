import random

def inject_attack(normal_events, attack_events, start_ratio=0.6):
    start = int(len(normal_events) * start_ratio)
    mixed = normal_events[:start]

    for e in attack_events:
        if random.random() < 0.3:  # stealth blending
            mixed.append(e)
        else:
            mixed.append(random.choice(normal_events))

    return mixed
