# APEX-TV

Онлайн-кинотеатр на Django

## О проекте

`APEX-TV` — это API для управления фильмами, подписками, watchlist и пользователями. Проект построен на Django и DRF, использует PostgreSQL и раздельную конфигурацию настроек через `split-settings`.

### Используемые технологии

- `Django`
- `Django REST Framework`
- `PostgreSQL`
- `python-dotenv`
- `split-settings`

## Структура проекта

- `movie` — фильмы, жанры и связи с подписками
- `subscription` — тарифы подписок
- `watchlist` — список фильмов пользователя
- `users` — кастомная модель пользователя
- `cinema` — корневые настройки и маршрутизация

## Основные сущности

### `Genre`
Справочник жанров для фильмов.

Содержит:

- `title` — название жанра
- `description` — описание жанра
- `slug` — URL-идентификатор жанра

### `Movie`
Содержит:

- `title` — название фильма
- `description` — описание
- `duration` — длительность
- `genre` — жанр
- `release_date` — дата выхода
- `subscriptions` — доступные подписки
- `poster_url` — ссылка на постер
- `trailer_url` — ссылка на трейлер
- `film_url` — ссылка на фильм

### `Subscription`
Содержит:

- `title` — название подписки
- `monthly_price` — цена подписки
- `max_video_quality` — максимальное качество видео (`480p`, `720p`, `1080p`, `4k`)

### `Watchlist`
Содержит:

- `user` — пользователь
- `movie` — фильм
- `created_at` — дата добавления
- `is_watched` — отмечен ли фильм как просмотренный

Ограничение: один и тот же фильм можно добавить в watchlist пользователя только один раз.

### `User`
Кастомная модель пользователя с дополнительными полями:

- `full_name`
- `phone`
- `email`
- `current_subscription`
- `watchlist`

## API

Все API-маршруты подключены с префиксом `/api/`.

- `/api/movie/` — CRUD для фильмов
- `/api/subscription/` — CRUD для подписок
- `/api/watchlist/` — CRUD для watchlist пользователя

## Возможности API

### `movie`

- стандартный `ModelViewSet`
- полное управление фильмами через REST
- пагинация, фильтрация и сортировка по полям `title`, `release_date`, `genre`

### `subscription`

- `ModelViewSet`
- пагинация
- поиск по названию
- сортировка по `id`, `monthly_price`, `title`
- валидация цены: значение должно быть больше 0

### `watchlist`

- доступ только для авторизованных пользователей
- фильтрация записей по текущему пользователю
- сортировка по `created_at` и `id`
- защита от дублирования фильма в watchlist

## Админка

Доступна панель администратора:

- `/admin/`

Через админку можно управлять:

- фильмами
- жанрами
- подписками
- watchlist-записями

## База данных и окружение

Проект использует PostgreSQL. Параметры подключения читаются из переменных окружения:

- `DATABASE_NAME`
- `DATABASE_USER`
- `DATABASE_PASSWORD`
- `DATABASE_HOST`
- `DATABASE_PORT`

Для локального запуска можно использовать `docker-compose.yml`, где уже описан контейнер PostgreSQL.

Пример `.env`:

```env
DATABASE_NAME=cinema_db
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

## Установка и запуск

### 1. Поднять PostgreSQL

```bash
docker-compose up -d
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Применить миграции

```bash
python manage.py migrate
```

### 4. Создать суперпользователя

```bash
python manage.py createsuperuser
```

### 5. Запустить сервер разработки

```bash
python manage.py runserver
```



## Краткий отчет по проекту

В проекте реализован онлайн-кинотеатр с REST API для фильмов, подписок и пользовательского watchlist. Основные доменные сущности вынесены в отдельные приложения, а пользовательская модель расширена дополнительными полями для работы с подпиской и контактными данными. Для подписок добавлены поиск, сортировка и пагинация, а watchlist защищен от дублей и доступен только авторизованному пользователю.
