from celery import shared_task
from .models import Contact
from .service import send
from .functions import *


@shared_task
def bar():
    return 'Hello world!'


@shared_task
def send_spam_email(user_email):
    send(user_email)


@shared_task
def search_mtg_news():
    session, header = login_on_magic_site()
    news_title, news_text, news_type = parse_mtg_news(session, header)
    save_news(news_title, news_text, news_type)


@shared_task
def search_arena_news():
    session, header = login_on_magic_site()
    news_title, news_text, news_type = parse_arena_news(session, header)
    save_news(news_title, news_text, news_type)
