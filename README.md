# Hi there 👋

```python
import torch
import torch.nn as nn


class Wiriya(nn.Module):

    def __init__(self):
        super().__init__()
        self.name = "Wiriya Polchumni"
        self.role = "AI/ML Engineer"
        self.core = [
            "PyTorch", "Transformers",   # models
            "vLLM", "SGLang",            # serving
            "LangChain", "LangGraph",    # agents
            "Qdrant", "Pinecone",        # vector DB
            "Langfuse",                  # observability
        ]
        self.languages_spoken = ["th_TH", "en_US"]

    def forward(self, coffee: torch.Tensor) -> str:
        return "Thanks for dropping by, hope you find some of my work interesting."


me = Wiriya()
print(me(torch.ones(1)))  # ☕ in, ideas out
```
