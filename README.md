# hse_cb_tg
Telegram posts cluster analysis for HSE CB course

Репозиторий включает в себя исходный код: 

1) Парсера - bs4_parser.py
2) Загрузки sBERT'a и получения эмбеддиногов - bert_encoding.py
3) Кластеризации - Clustering.ipynb

Оюъединение всех компонент в пайплайн и его контейнеризацию

А так же данные:
-raw_tg_data.zip 

-tg_channels_clusters_2023_24_10.xlsx 

usage: 
docker build -t hse_cb_project .
docker run hse_cb_project
