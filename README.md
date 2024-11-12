# Кошачий благотворительный фонд

----
### Введение
Проект QRKot — приложение для Баготворительного фонда поддержки котов
Фонд может собирать на любые проекты пожертовования.<br>
**Проекты**<br>
В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект<br>
**Пожертвования**<br>
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.<br>
**Пользователи**<br>
Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

----
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Mrclive7406/cat_charity_fund
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте файл .env c содержимым:

```
APP_TITLE=Кошачий благотворительный фонд
DATABASE_URL=sqlite+aiosqlite:///./charity_project_donation.db 
```

Создать базу данных
```
alembic upgrade head
```

Запуск:

```
uvicorn app.main:app
```

Перейдите по url-адресу:

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Примеры запросов к API, варианты ответов и ошибок приведены в спецификации 
```openapi.json```; спецификация есть в корневой папке проекта cat_charity_found. 


## Автор 
- [Колесников Павел ](https://github.com/Mrclive7406)
# GitHub 
- [Проект парсинга pep и документации Python](https://github.com/Mrclive7406/cat_charity_fund)



- [Flask Api](https://flask-api.readthedocs.io/en/latest/)

Документация API проекта доступена по адресам:
- [Документация (Swagger)](http://127.0.0.1:8000/docs#)
- [Документация (Redoc)](http://127.0.0.1:8000/redoc#)

## Стек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastApi](https://img.shields.io/badge/-Fastapi-464646?logo=fastapi)](https://fastapi.tiangolo.com/)
[![FastApi-SQLAlchemy](https://img.shields.io/badge/-FastapiSQLAlchemy-464646?logo=fastapi)](https://fastapi.tiangolo.com/how-to/async-sql-encode-databases/?h=sqlalchemy#import-and-set-up-sqlalchemy)
[![Fastapi-Users](https://img.shields.io/badge/-Fastapi_Users-464646?logo=fastapi)](https://fastapi-users.github.io/fastapi-users/10.0/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?logo=Pydantic)](https://docs.pydantic.dev/latest/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)
