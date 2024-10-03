# Тестовое задание для CPA Traffic Light
Веб-страница, которая выводит древовидную структуру
отделов со списком сотрудников
Информация о каждом сотруднике  хранится в базе данных и
содержит следующие данные:
- ФИО;
- Должность;
- Дата приема на работу;
- Размер заработной платы;
- Подразделение - подразделения имеют структуру до 5 уровней;
Дерево отображается в свернутом виде.

## Перед установкой
В операционной системе должен стоять Docker compose

## Установка
Скопировать репозиторий

Перейти в папку 
```commandline
cd cpatl_test
```

Запустить команду 
```commandline
docker compose up -d --build
```

Создать файл .env по примеру:
```
DJANGO_SECRET_KEY=key
SQL_ENGINE=django.db.backends.postgresql_psycopg2
DATABASE=postgres
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=db
DATABASE_PORT=5432
```
С этого момента сервис доступен по адресу 127.0.0.1:8000/employees/

## После установки
Для создания аккаунта доступа в админку:
```commandline
docker compose exec cpatl python manage.py createsuperuser
```
Админка доступна по адресу 127.0.0.1:8000/admin/

Для наполнения таблицы подразделениями предприятия:
```commandline
docker compose exec cpatl python manage.py create_subdivisions     
```
Для наполнения таблицы сотрудниками (аргумент num_employees опционален, значение по умолчанию 60000):
```commandline
docker compose exec cpatl python manage.py create_employees --num_employees 15
```



