# hse_cb_tg
Telegram posts cluster analysis for HSE CB course

Репозиторий включает в себя исходный код: 

1) Парсера
2) Загрузки sBERT'a
3) Кластеризации

Оюъединение всех компонент в пайплайн и его контейнеризацию

usage: 
docker build -t hse_cb_project .
docker run hse_cb_project
