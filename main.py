import bert_encoding
import bs4_parser
import k_means_inference
import numpy as np
import pandas as pd
from time import gmtime, strftime

centroids = np.load("centroids.npy")
urls_tg = [
    "https://rsshub.app/telegram/channel/banksta",
    "https://rsshub.app/telegram/channel/AlfaBank",
    "https://rsshub.app/telegram/channel/centralbank_russia",
    "https://rsshub.app/telegram/channel/M24_Dengi",
    "https://rsshub.app/telegram/channel/financelist",
    "https://rsshub.app/telegram/channel/Finindie",
    "https://rsshub.app/telegram/channel/sberbank",
    "https://rsshub.app/telegram/channel/SberInvestments",
    "https://rsshub.app/telegram/channel/suverenka",
    "https://rsshub.app/telegram/channel/tinkoffbank",
    "https://rsshub.app/telegram/channel/tinkoff_invest_official",
    "https://rsshub.app/telegram/channel/bankvtb",
]
# parsing raw texts
raw_texts = bs4_parser.all_news_per_day(urls_tg)
# getting embeddings with bert
embeddings = bert_encoding.bert_encoding(raw_texts)
# k-means inference
clusters = k_means_inference.get_clusters(embeddings)
# computing clustering metrics
metrics = k_means_inference.compute_metrics(embeddings, clusters)

pd.DataFrame({"Texts": raw_texts, "Clusters": clusters}).to_excel(
    f'tg_channels_clusters_{strftime("%Y_%d_%m", gmtime())}.xlsx', index=False
)
