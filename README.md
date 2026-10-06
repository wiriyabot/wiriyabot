### Hi there 👋

```python
import torch
import torch.nn as nn


class Wiriya(nn.Module):

    def __init__(self):
        super().__init__()
        self.name = "Wiriya Polchumni"
        self.role = "AI Engineer"
        self.focus = ["LLM Agents", "RAG", "Thai NLP"]
        self.stack = {
            "deep_learning": ["PyTorch", "TensorFlow", "scikit-learn", "Transformers"],
            "llm_serving": ["vLLM", "SGLang"],
            "agents": ["LangChain", "LangGraph"],
            "vector_db": ["Qdrant"],
        }
        self.languages_spoken = ["th_TH", "en_US"]

    def forward(self, coffee: torch.Tensor) -> str:
        return "Thanks for dropping by, hope you find some of my work interesting."


me = Wiriya()
print(me(torch.ones(1)))  # ☕ in, ideas out
```
