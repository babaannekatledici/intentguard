import time

def stream(events, delay=0.05):
    for e in events:
        yield e
        time.sleep(delay)
