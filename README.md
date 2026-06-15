# Итоговое ДЗ. Модуль 4. Экзамен ETL

## Студент

Кондратьев Владислав

## Описание

Репозиторий содержит материалы итоговой практической работы по модулю 4 дисциплины ETL-процессы.

## Задача 1. Yandex Data Transfer: YDB → Object Storage

В рамках задачи выполняется перенос данных из Managed Service for YDB в Yandex Object Storage с использованием Yandex Data Transfer.

### Что сделано

1. Подготовлен генератор тестовых данных `transactions_v2`.
2. Сгенерирован CSV-файл `transactions_v2.csv` объёмом 36.41 МБ.
3. Подготовлен YQL-скрипт создания таблицы в YDB.
4. Подготовлен YQL-скрипт проверки данных.
5. Далее данные будут загружены в YDB и перенесены в Object Storage через Data Transfer.

### Структура проекта

```text
scripts/generate_transactions_v2.py       # генератор CSV-файла
yql/01_create_transactions_v2.yql         # создание таблицы transactions_v2
yql/02_check_transactions_v2.yql          # проверка количества строк
docs/                                     # отчёты
screenshots/                              # скриншоты выполнения
data/                                     # локальные данные, CSV не хранится в Git