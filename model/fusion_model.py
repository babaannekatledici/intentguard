import torch
import torch.nn as nn

class FusionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(16 + 3, 16)

    def forward(self, seq_emb, graph_emb):
        combined = torch.cat([seq_emb, graph_emb], dim=1)
        return self.fc(combined)
