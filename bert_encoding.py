from transformers import AutoTokenizer, AutoModel
from typing import List
import numpy as np

device = "cpu"
tokenizer = AutoTokenizer.from_pretrained("sberbank-ai/sbert_large_nlu_ru")
model = AutoModel.from_pretrained("sberbank-ai/sbert_large_nlu_ru")


def encode(text: List):
    """
    tokenizing + creating embeddings
    :param text: List of raw data
    :return: np array of embeddings
    """
    encoding = tokenizer(
        text, padding=True, return_tensors="pt", max_length=512, truncation=True
    )
    return model(**encoding).pooler_output.cpu().detach().numpy()


def bert_encoding(texts: List) -> np.array:
    """
    Build embeddings for cluster analysis
    :param texts: raw texts after parsing: List
    :return: np array of embeddings
    """
    # empty array for batching
    X_all = np.zeros([1, 1024])

    for text in range(0, len(texts), 2):
        X_all = np.append(X_all, encode(texts[text : text + 2]), axis=0)
    return X_all[1:, :]
