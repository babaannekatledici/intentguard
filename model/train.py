import torch
from .intent_encoder import IntentEncoder
from .fusion_model import FusionModel

def train(sequences, graphs, vocab_size):
    enc = IntentEncoder(vocab_size)
    fusion = FusionModel()
    opt = torch.optim.Adam(
        list(enc.parameters()) + list(fusion.parameters()), lr=1e-3
    )

    for seq, graph in zip(sequences, graphs):
        x = torch.tensor(seq).unsqueeze(0)
        g = torch.tensor(graph).unsqueeze(0).float()

        seq_emb = enc(x)
        fused = fusion(seq_emb, g)

        loss = fused.norm()
        opt.zero_grad()
        loss.backward()
        opt.step()

    return enc, fusion
