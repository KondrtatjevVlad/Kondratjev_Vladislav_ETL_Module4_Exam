# Отчёт по задаче 1

## Цель

Перенести данные из Managed Service for YDB в Object Storage с использованием сервиса Yandex Data Transfer.

## Исходные данные

Для выполнения задачи была подготовлена таблица `transactions_v2`.

Структура таблицы:

| Поле | Описание |
|---|---|
| call_id | идентификатор звонка |
| call_time | время звонка |
| client_id | идентификатор клиента |
| region_code | код региона |
| campaign_type | тип кампании |
| call_status | статус звонка |
| client_response | ответ клиента |
| duration_sec | длительность звонка |
| follow_up_required | требуется ли повторный контакт |

CSV-файл был сгенерирован скриптом `scripts/generate_transactions_v2.py`.

Объём файла: более 30 МБ.

## Создание таблицы YDB

Таблица была создана с помощью YQL-скрипта:

`yql/01_create_transactions_v2.yql`

## Загрузка данных

Данные были загружены в YDB через YDB CLI командой импорта CSV.

После загрузки была выполнена проверка количества строк с помощью скрипта:

`yql/02_check_transactions_v2.yql`

## Data Transfer

Для переноса были созданы:

- source endpoint: YDB
- target endpoint: Object Storage
- transfer type: Snapshot

После запуска трансфера статус изменился на `Completed`.

## Проверка результата

В бакете Object Storage появилась папка `from_ydb`, внутри которой находится CSV-файл с выгруженными данными из таблицы `transactions_v2`.

## Вывод

Задача выполнена: данные из Managed Service for YDB успешно перенесены в Object Storage с использованием Yandex Data Transfer.