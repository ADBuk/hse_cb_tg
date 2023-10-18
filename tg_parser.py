from telethon.sync import TelegramClient, events
from collections import deque
from typing import List

# параметры краулера
# список ссылок на все тг каналы
urls_tg = [
    "https://t.me/banksta",
    "https://t.me/AlfaBank",
    "https://t.me/centralbank_russia",
    "https://t.me/M24_Dengi",
    "https://t.me//financelist",
    "https://t.me//Finindie",
    "https://t.me//sberbank",
    "https://t.me//SberInvestments",
    "https://t.me//suverenka",
    "https://t.me//tinkoffbank",
    "https://t.me//tinkoff_invest_official",
    "https://t.me//bankvtb",
]
session_name = "tg_parser"
api_id = 123123  ##########
api_hash = ""  ############

# Сессия клиента telethon
posted_q = deque(maxlen=20)


def telegram_parser(
    session_name: str,
    api_id: int,
    api_hash: str,
    telegram_channels: List,
    posted_q,
    n_test_chars: int = 50,
    logger=None,
    loop=None,
):
    """
    Tg parser for news channels
    :param session_name: имя сессии для телеграма
    :param api_id: айпи айди с tg.org
    :param api_hash: айпи хеша с tg.org
    :param telegram_channels: список ссылок на тг каналы
    :param posted_q: Очередь уже опубликованных постов
    :param n_test_chars: ключ для поиска повторных постов по n символов
    :param logger: Параметр логгера телеграма
    :param loop: asyncio.new_event_loo
    :return: тг клиент
    """

    # Ссылки на телеграм каналы
    telegram_channels_links = telegram_channels

    client = TelegramClient(
        session_name, api_id, api_hash, base_logger=logger, loop=loop
    )
    client.start()

    @client.on(events.NewMessage(chats=telegram_channels_links))
    async def handler(event):
        """
        Возвращает спаршенный текст с тг канала
        :param event: tg session event
        :return: text
        """
        if event.raw_text == "":
            return

        news_text = " ".join(event.raw_text.split("\n")[:2])

        head = news_text[:n_test_chars].strip()

        if head in posted_q:
            return
        print(news_text)
        return news_text

    return client


if __name__ == "__main__":
    client = telegram_parser(session_name, api_id, api_hash, urls_tg, posted_q)

    client.run_until_disconnected()
