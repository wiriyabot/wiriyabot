# Hi there 👋

```python
import torch
import torch.nn as nn


class Wiriya(nn.Module):

    def __init__(self):
        super().__init__()
        self.name = "Wiriya Polchumni"
        self.role = "AI/ML Engineer"
        self.stack = {
            "deep_learning": ["PyTorch", "TensorFlow", "scikit-learn", "Transformers"],
            "fine_tuning": ["LoRA / QLoRA"],
            "llm_serving": ["vLLM", "SGLang", "llama.cpp"],
            "agents": ["LangChain", "LangGraph", "LlamaIndex"],
            "vector_db": ["Qdrant", "Pinecone", "FAISS"],
            "llm_ops": ["LangSmith", "Langfuse", "MLflow"],
            "deployment": ["FastAPI", "Docker"],
        }
        self.languages_spoken = ["th_TH", "en_US"]

    def forward(self, coffee: torch.Tensor) -> str:
        return "Thanks for dropping by, hope you find some of my work interesting."


me = Wiriya()
print(me(torch.ones(1)))  # ☕ in, ideas out
```
