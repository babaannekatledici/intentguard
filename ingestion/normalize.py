def normalize(events):
    vocab = {e:i for i,e in enumerate(sorted(set(events)))}
    encoded = [vocab[e] for e in events]
    return encoded, vocab
