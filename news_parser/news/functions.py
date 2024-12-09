import requests
import fake_useragent
from bs4 import BeautifulSoup
from .models import *
from .service import send_news_email


def login_on_magic_site():
    session = requests.Session()
    link = f"https://myaccounts.wizards.com/api/login"
    user = fake_useragent.UserAgent().random

    header = {
        'user-agent': user,
    }

    data = {
        'username': "username",
        'password': "your_password"
    }

    responce = session.post(link, data=data, headers=header)
    return session, header


def parse_mtg_news(session: requests.Session, header: dict):
    news_link = 'https://magic.wizards.com/ru/news'
    news_text = session.get(news_link, headers=header).text
    soup = BeautifulSoup(news_text, 'lxml')
    block = soup.find('div', class_="swiper-wrapper")
    latest_new = block.find('div', class_="swiper-slide")
    news_title = latest_new.find('div', class_="css-MLQMg").find('h3', class_="css-+V4Kd css-05n0D").text
    news_text = latest_new.find('div', class_="css-MLQMg").find('div', class_="css-sHFQF").text
    return news_title, news_text, "Mtg"


def parse_arena_news(session: requests.Session, header: dict):
    news_link = 'https://magic.wizards.com/ru/mtgarena'
    news_text = session.get(news_link, headers=header).text
    soup = BeautifulSoup(news_text, 'lxml')
    block = soup.find('div', class_='css-X2cbA')
    latest_new = block.find('div', class_='css-uehwQ')
    news_title = latest_new.find('div', class_='css-MLQMg').find('h3', class_="css-+V4Kd css-05n0D").text
    news_text = latest_new.find('div', class_='css-MLQMg').find('div', class_="css-sHFQF").text
    return news_title, news_text, "Arena"


def save_news(news_title, news_text, news_type):
    all_news = MagicNews.objects.all()
    mtg_subscription = NewsType.objects.get(type=news_type)
    users_email = list(User.objects.filter(contact__subscription=mtg_subscription).values_list('email', flat=True))
    for news in all_news:
        if news_title == news.title:
            return
    magic_news = MagicNews(title=news_title, text=news_text, type=mtg_subscription)
    magic_news.save()
    for user_email in users_email:
        send_news_email(user_email, news_title, mtg_subscription)
