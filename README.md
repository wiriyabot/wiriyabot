<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/wave-dark.png">
    <img src="assets/wave.png" width="140" alt="A little black blob waving hello">
  </picture>
</p>

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

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/sleepy-dark.png">
    <img src="assets/sleepy.png" width="110" alt="Blob sleeping">
  </picture>
</p>
