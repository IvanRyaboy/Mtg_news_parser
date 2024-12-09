# Mtg_news_parser

## Установка
Для установки проекта выполните следующие шаги:

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/IvanRyaboy/Mtg_news_parser.git
   cd Mtg_news_parser
2. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
  **Для того, чтобы запустить celery worker на windows:**
   ```bash
   celery -A news_parser worker -l info --pool=solo
  ```
**Для запуска Redis откройте Docker и выполните следующую команду:**
```bash
docker run --name some-redis -p 16379:6379 -d redis
