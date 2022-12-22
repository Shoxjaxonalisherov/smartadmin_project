import requests
from bs4 import BeautifulSoup
import re

def gazeta_news_base():
    """Данная функция выполняет следующие действия:

        1. Отправляет HTTP-запрос с помощью библиотеки requests на указанный URL: https://www.gazeta.ru/sport/football/
        2. Парсит HTML-страницу, используя библиотеку BeautifulSoup и парсер html.parser.
        3. Извлекает ссылку на новость с главной страницы раздела "Спорт" сайта "Газета".
        4. Формирует полную ссылку на новость, добавляя к извлеченной ссылке домен сайта.
        5. Отправляет новый HTTP-запрос на сформированную ссылку.
        6. Парсит HTML-страницу новости, используя библиотеку BeautifulSoup и парсер html.parser."""

    r = requests.get('https://www.gazeta.ru/sport/football/')
    html = BeautifulSoup(r.content, 'html.parser')
    news_html = html.find("div", class_="b_newslist-digest").find("a", class_="b_ear m_simple")
    get_link_from_html = news_html.get("href")
    link_of_news = ("https://www.gazeta.ru" + get_link_from_html)
    r2 = requests.get(link_of_news)
    r2_html = BeautifulSoup(r2.content, "html.parser")
    return r2_html

def gazeta_news_header():
    """Данная функция выполняет следующие действия:
        1. Вызывает функцию gazeta_news_base(), которая возвращает HTML-страницу новости.
        2. Извлекает заголовок новости из HTML-страницы с помощью метода find объекта BeautifulSoup.
        3. Добавляет к заголовку символ "⚡" и возвращает результат в виде строки."""

    r2_header = gazeta_news_base().find("div", class_="b_article-header")\
        .find("h1", class_="headline")
    return ("⚡" + r2_header.text.strip() + '.\n')

def gazeta_news_text():
    """Данная функция выполняет следующие действия:

        1. Вызывает функцию gazeta_news_base(), которая возвращает HTML-страницу новости.
        2. Извлекает текст новости из HTML-страницы с помощью метода find_all объекта BeautifulSoup.
        3. Формирует текст новости из извлеченных блоков текста, добавляя к нему строку с информацией об источнике.
        4. Возвращает текст новости в виде строки."""

    r2_text_location = gazeta_news_base()\
        .find("div", class_="b_article-text")\
        .find_all("p")
    r2_text = ""
    for i in r2_text_location:
        r2_text += "\n\n" + i.text
    r2_text += ('<i> - Передаёт АО "Газета.Ру" </i>')
    return r2_text.strip()

def gazeta_image():
    """Данная функция выполняет следующие действия:

       1. Вызывает функцию gazeta_news_base(), которая возвращает HTML-страницу новости.
       2. Извлекает ссылку на изображение из HTML-страницы с помощью метода find объекта BeautifulSoup.
       3. Возвращает ссылку на изображение в виде строки."""

    image = gazeta_news_base().find("div", class_="b_article-media")\
            .find("div", class_="mainarea-wrapper")\
            .find("img").get("data-hq")
    return image

def ria_news_base():
    """Данная функция выполняет следующие действия:

        1. Отправляет HTTP-запрос с помощью библиотеки requests на указанный URL: https://rsport.ria.ru/football/
        2. Парсит HTML-страницу, используя библиотеку BeautifulSoup и парсер html.parser.
        3. Извлекает ссылку на новость с главной страницы раздела "Спорт" сайта "РИА".
        4. Формирует полную ссылку на новость, добавляя к извлеченной ссылке домен сайта.
        5. Отправляет новый HTTP-запрос на сформированную ссылку.
        6. Парсит HTML-страницу новости, используя библиотеку BeautifulSoup и парсер html.parser."""

    r = requests.get('https://rsport.ria.ru/football/')
    html = BeautifulSoup(r.content, 'html.parser')
    news_html = html.find("div", class_="layout-rubric")\
        .find("div", class_="rubric-list")\
        .find("div", class_="list")\
        .find("div", class_="list-item")\
        .find("a", itemprop="url")\
        .get("href")

    link_of_news = news_html
    r3 = requests.get(link_of_news)
    r3_html = BeautifulSoup(r3.content, "html.parser")
    return r3_html

def ria_news_header():
    """Данная функция выполняет следующие действия:
            1. Вызывает функцию ria_news_base(), которая возвращает HTML-страницу новости.
            2. Извлекает заголовок новости из HTML-страницы с помощью метода find объекта BeautifulSoup.
            3. Добавляет к заголовку символ "⚡" и возвращает результат в виде строки."""

    r3_header = ria_news_base() \
        .find("div", class_="article__title")

    return ("⚡" + r3_header.text.strip() + "\n")

def ria_news_text():
    """Данная функция выполняет следующие действия:

            1. Вызывает функцию ria_news_base(), которая возвращает HTML-страницу новости.
            2. Извлекает текст новости из HTML-страницы с помощью метода find_all объекта BeautifulSoup.
            3. Формирует текст новости из извлеченных блоков текста, добавляя к нему строку с информацией об источнике.
            4. Возвращает текст новости в виде строки."""

    r3_text_location = ria_news_base()\
        .find("div", class_= "article__body js-mediator-article mia-analytics")\
        .find_all("div", class_="article__text")
    r3_text = ""
    for i in r3_text_location:
        r3_text += "\n\n" + i.text
    r3_text = re.sub(r'МОСКВА, .. дек - РИА Новости.', '', r3_text)
    r3_text += ('<i> - Сообщает РИА Новости </i>')
    return r3_text.strip()

def ria_news_image():
    """Данная функция выполняет следующие действия:

           1. Вызывает функцию ria_news_base(), которая возвращает HTML-страницу новости.
           2. Извлекает ссылку на изображение из HTML-страницы с помощью метода find объекта BeautifulSoup.
           3. Возвращает ссылку на изображение в виде строки."""

    image = ria_news_base().find("div", class_= "article__announce")\
        .find("div", class_="media__size")\
        .find("img")\
        .get("src")
    return image