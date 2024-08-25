import torch
from transformers import AutoModel, AutoTokenizer

# 从根目录下加载模型和分词器
def load_model_and_tokenizer(model_path='./models/model'):
    model = AutoModel.from_pretrained(model_path, trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model.eval()
    return model, tokenizer



