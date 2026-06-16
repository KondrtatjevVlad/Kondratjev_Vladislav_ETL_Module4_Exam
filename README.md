# Итоговое ДЗ. Модуль 4. Экзамен ETL

## Задача 1. Yandex Data Transfer: YDB → Object Storage

В рамках задачи была реализована загрузка данных `transactions_v2` в Managed Service for YDB и перенос этих данных в Yandex Object Storage с использованием Yandex Data Transfer.

## Что сделано

1. Создана база данных Yandex Database / Managed Service for YDB.
2. Сгенерирован CSV-файл `transactions_v2.csv` объёмом 36.4 МБ.
3. В YDB создана таблица `transactions_v2`.
4. Данные загружены в таблицу через YDB CLI.
5. Создан бакет Object Storage.
6. Созданы endpoint-источник YDB и endpoint-приёмник Object Storage.
7. Создан и запущен transfer типа Snapshot.
8. Проверено появление CSV-файла в Object Storage.

## Структура проекта

- `scripts/generate_transactions_v2.py` — генератор тестовых данных.
- `yql/01_create_transactions_v2.yql` — создание таблицы YDB.
- `yql/02_check_transactions_v2.yql` — проверка количества строк.
- `docs/report_task_1.md` — отчёт по задаче 1.
- `screenshots` — скриншоты выполнения.
=======
- `task_1/scripts/generate_transactions_v2.py` — генератор тестовых данных.
- `task_1/yql/01_create_transactions_v2.yql` — создание таблицы YDB.
- `task_1/yql/02_check_transactions_v2.yql` — проверка количества строк.
- `task_1/docs/report_task_1.md` — отчёт по задаче 1.
- `task_1/screenshots/` — скриншоты выполнения.

## Использованные сервисы

- Yandex Managed Service for YDB
- Yandex Object Storage
- Yandex Data Transfer
- YDB CLI
- Yandex Cloud CLI
