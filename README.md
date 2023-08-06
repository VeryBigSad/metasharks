# Metasharks

Тестовое задание для Metasharks, организация учебного процесса в ВУЗе.

Запуск проекта

- Через Докер: `docker compose up -d`
- Не через Докер: `python virtualenv venv && venv/scripts/activate && pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000`

Проект будет запущен на порте 8000.

Реализованы модели и ручки, описанные в ТЗ. Для удобства подключен swagger на http://localhost:8000/swagger.

Управление студентами/учебными группами у Кураторов (как и у администрации) подразумевается через REST API.

Есть отдельная celery таска (асинхронная задача) для создания excel отчетов; она вызывается на post_save сигнале при создании модельки `Report`.

При разработке проекта использовался pre-commit, весь проект проходит проверку flake8 и mypy.

В качестве брокера сообщений используется `Redis`.


#### Contacts

[Мой телеграм](https://t.me/mikhail_khromov)
