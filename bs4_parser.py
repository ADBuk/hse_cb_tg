import requests
from bs4 import BeautifulSoup
import re
from typing import List

# parsing garbage
chars_to_remove = ["<br>", "</u>", "</a>", "</b>", "</i>", "tg-emoj", "&nsp"]
# for rus texts only
r = re.compile("[а-яА-Я]+")
# re for deleting garbage
rx = "[" + re.escape("".join(chars_to_remove)) + "]"


def get_tg_clean_texts(url: str) -> List:
    """
    Parse RSS of Tg channel and rerurn all posts per 1 day
    :param url: url to tg channel using the rss website
    :return: List of cleaned texts
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, features="xml")

    news_items = soup.find_all("description")

    # cleaning forwarded from messages
    texts = []
    for i in news_items[1:]:  # starting from 1 because of xml specification
        if i.text.find("Forwarded From") == -1:
            texts.append(i.text)
    # we will use only russian texts (SBERT Large)
    rus = []
    for i in range(0, len(texts)):
        rus.append(" ".join([w for w in filter(r.match, texts[i].split(" "))]))

    # Deliting all parse garbage
    clean_news = []
    for i in rus:
        clean_news.append(re.sub(rx, "", i).replace(";", " "))

    return clean_news


def all_news_per_day(urls: List) -> List:
    """
    Getting all news from tg channels
    :param urls: List of links of tg channels
    :return: List of all texts to BERT
    """
    texts = []
    for i in urls:
        texts.extend(get_tg_clean_texts(i))

    return texts
