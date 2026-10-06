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

![Python](https://img.shields.io/badge/Python-1f2328?style=flat-square&logo=python&logoColor=FFD43B) ![PyTorch](https://img.shields.io/badge/PyTorch-1f2328?style=flat-square&logo=pytorch&logoColor=EE4C2C) ![TensorFlow](https://img.shields.io/badge/TensorFlow-1f2328?style=flat-square&logo=tensorflow&logoColor=FF6F00) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1f2328?style=flat-square&logo=scikitlearn&logoColor=F7931E) ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-1f2328?style=flat-square&logo=huggingface&logoColor=FFD21E) ![LangChain](https://img.shields.io/badge/LangChain-1f2328?style=flat-square&logo=langchain&logoColor=FFFFFF) ![LangGraph](https://img.shields.io/badge/LangGraph-1f2328?style=flat-square&logo=langgraph&logoColor=FFFFFF) ![FastAPI](https://img.shields.io/badge/FastAPI-1f2328?style=flat-square&logo=fastapi&logoColor=009688) ![Docker](https://img.shields.io/badge/Docker-1f2328?style=flat-square&logo=docker&logoColor=2496ED) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-1f2328?style=flat-square&logo=postgresql&logoColor=4169E1) ![Supabase](https://img.shields.io/badge/Supabase-1f2328?style=flat-square&logo=supabase&logoColor=3FCF8E) ![Pandas](https://img.shields.io/badge/Pandas-1f2328?style=flat-square&logo=pandas&logoColor=E70488) ![NumPy](https://img.shields.io/badge/NumPy-1f2328?style=flat-square&logo=numpy&logoColor=4DABCF)
