# Youtube-Downloader-Bot 
## Об проекте
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yt_dlp)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiogram)



Простой бот который занимается установкой видео с youtube

## Устоновка (GNU/Linux)

```bash
git clone https://github.com/ZeroNiki/Youtube-Downloader-Bot.git 
```

Перейдите в папку Youtube-Downloader-Bot и создадите вертуальное окружение:

```bash
cd Youtube-Downloader-Bot
python3 -m venv venv && source venv/bin/activate
```

Устоновите зависимости:

```bash
pip install -r requirements.txt
```

## Конфигурация

Сначала получите токен своего бота в @botfather. Затем создадите файл config.py, а в ней переменую TOKEN и вставсте токен вашего бота(в кавычки):

```python
TOKEN = 'Токен вашего бота'
```

Запускае main.py

### Внимание!
**!Бот устанавливает файлы в вашу деректорю где лежит этот код**

### Планы на проект
 - ~~Отправка файла пользователю~~
 - Конвертировать в .mp3
 - Inline кнопки

