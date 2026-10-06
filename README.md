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
        self.stack = ["PyTorch", "Transformers", "LangGraph", "LangChain"]
        self.languages_spoken = ["th_TH", "en_US"]

    def forward(self, coffee: torch.Tensor) -> str:
        return "Thanks for dropping by, hope you find some of my work interesting."


me = Wiriya()
print(me(torch.ones(1)))  # ☕ in, ideas out
```

![Python](https://img.shields.io/badge/Python-1f2328?style=flat-square&logo=python&logoColor=FFD43B) ![PyTorch](https://img.shields.io/badge/PyTorch-1f2328?style=flat-square&logo=pytorch&logoColor=EE4C2C) ![TensorFlow](https://img.shields.io/badge/TensorFlow-1f2328?style=flat-square&logo=tensorflow&logoColor=FF6F00) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1f2328?style=flat-square&logo=scikitlearn&logoColor=F7931E) ![Transformers](https://img.shields.io/badge/Transformers-1f2328?style=flat-square&logo=huggingface&logoColor=FFD21E) ![PEFT](https://img.shields.io/badge/PEFT-1f2328?style=flat-square&logo=huggingface&logoColor=FFD21E) ![vLLM](https://img.shields.io/badge/vLLM-1f2328?style=flat-square&logo=vllm&logoColor=FDB515) ![SGLang](https://img.shields.io/badge/SGLang-1f2328?style=flat-square) ![LangChain](https://img.shields.io/badge/LangChain-1f2328?style=flat-square&logo=langchain&logoColor=FFFFFF) ![LangGraph](https://img.shields.io/badge/LangGraph-1f2328?style=flat-square&logo=langgraph&logoColor=FFFFFF) ![Qdrant](https://img.shields.io/badge/Qdrant-1f2328?style=flat-square&logo=qdrant&logoColor=DC244C)
