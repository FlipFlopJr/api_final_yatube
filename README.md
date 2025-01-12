## Проект «API для Yatube»

Yatube - проект социальной сети. Лавринович Андрей. Финансовый университет.

### Реализованы возможности

- API позволяет получать список публикаций, создавать новые, редактировать существующие и удалять ненужные.
-  Пользователи могут получать комментарии к публикациям, добавлять свои, изменять и удалять уже написанные.
-  API предоставляет доступ к информации о существующих сообществах, включая детальную информацию о каждом из них.
- Пользователи могут просматривать свои подписки на авторов, а также подписываться на интересующих их авторов.
- Получение, обновление и проверка JWT авторизации.

### Технологии

- [Python](https://www.python.org/) - язык программирования.
- [Django](https://www.djangoproject.com/) - свободный фреймворк для веб-приложений на языке Python.
- [Django REST Framework](https://www.django-rest-framework.org/) - мощный и гибкий набор инструментов для создания веб-API.
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - плагин аутентификации JSON Web Token для Django REST Framework.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/FlipFlopJr/api_final_yatube`

`cd api_final_yatube`


Создать и активировать виртуальное окружение:

+ `python -m venv venv`
+ `source venv/bin/activate`
+ `python -m pip install --upgrade pip`

Установить зависимости из файла requirements.txt:
`pip install -r requirements.txt`

Выполнить миграции:
`python manage.py migrate`


Запустить проект:
`python manage.py runserver`
#### После запуска проекта, документация будет доступна по адресу:
`http://localhost:port/redoc/`

