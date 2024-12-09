from django.core.mail import send_mail


def send(user_email):
    send_mail(
        "Вы подписались на уведомления",
        "Мы будем присылать вам много спама",
        "elex34231997@gmail.com",
        [user_email,],
        fail_silently=False,
    )


def send_news_email(user_email, news_title, news_type):
    send_mail(
        f"На сайте появилась новая новость о {news_type}",
        f"{news_title}",
        "elex34231997@gmail.com",
        [user_email,],
        fail_silently=False,
    )

