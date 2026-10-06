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

![Python](https://img.shields.io/badge/Python-1f2328?style=flat-square&logo=python&logoColor=FFD43B) ![PyTorch](https://img.shields.io/badge/PyTorch-1f2328?style=flat-square&logo=pytorch&logoColor=EE4C2C) ![TensorFlow](https://img.shields.io/badge/TensorFlow-1f2328?style=flat-square&logo=tensorflow&logoColor=FF6F00) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1f2328?style=flat-square&logo=scikitlearn&logoColor=F7931E) ![Transformers](https://img.shields.io/badge/Transformers-1f2328?style=flat-square&logo=huggingface&logoColor=FFD21E) ![PEFT](https://img.shields.io/badge/PEFT-1f2328?style=flat-square&logo=huggingface&logoColor=FFD21E) ![vLLM](https://img.shields.io/badge/vLLM-1f2328?style=flat-square&logo=vllm&logoColor=FDB515) ![SGLang](https://img.shields.io/badge/SGLang-1f2328?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjEwMCA3MCA2MDAgNjYwIj48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNFODY3M0MiIHN0cm9rZS13aWR0aD0iNDQiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTI5MCAzNzVDMzUwIDM4MCA0MjUgNDYwIDQzMiA1NzUiLz48cGF0aCBkPSJNMzkwIDQzMkM1MDAgNDIwIDU4NSAzNDUgNTg1IDI1NSIvPjxjaXJjbGUgY3g9IjIxMiIgY3k9IjM3NSIgcj0iODAiIGZpbGw9IiNGQUQ5QzgiLz48Y2lyY2xlIGN4PSI1ODUiIGN5PSIxNzAiIHI9IjgwIiBmaWxsPSIjRkFEOUM4Ii8+PHJlY3QgeD0iMzM1IiB5PSI1NzUiIHdpZHRoPSIxOTAiIGhlaWdodD0iMTMwIiByeD0iMjYiIGZpbGw9IiNGQUQ5QzgiLz48cGF0aCBkPSJNMzk1IDYxNWwtMjUgMjUgMjUgMjVNNDY1IDYxNWwyNSAyNS0yNSAyNU00NDIgNjEwbC0yMiA2MCIgc3Ryb2tlLXdpZHRoPSIyMiIvPjwvZz48L3N2Zz4K) ![LangChain](https://img.shields.io/badge/LangChain-1f2328?style=flat-square&logo=langchain&logoColor=FFFFFF) ![LangGraph](https://img.shields.io/badge/LangGraph-1f2328?style=flat-square&logo=langgraph&logoColor=FFFFFF) ![Qdrant](https://img.shields.io/badge/Qdrant-1f2328?style=flat-square&logo=qdrant&logoColor=DC244C)
