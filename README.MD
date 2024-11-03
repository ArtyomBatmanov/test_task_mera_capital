## Тестовое задание на позицию junior back-end разработчика

### Задание:

1. Написать для криптобиржи Deribit (https://docs.deribit.com/)
асинхронный клиент на aiohhtp. Клиент должен каждую минуту забирать
с биржи текущую цену btc_usd и eth_usd (index price валюты) после
чего сохранять в базу данных тикер валюты, текущую цену и время в
UNIX timestamp.

2. Написать внешнее API для обработки сохраненных данных на FastAPI.
Обязательные требования:
1) API должно включать в себя следующие методы:
- Получение всех сохраненных данных по указанной валюте
- Получение последней цены валюты
- Получение цены валюты с фильтром по дате
Все методы должны быть GET и у каждого метода дожен быть
обязятельный query-параметр "ticker".
2) Код выложить на гитхаб с подробным readme и документацией по разворачиванию.
Можно использовать любую БД на выбор для хранения цен.
3) 
Необязательные требования:
1. Написать тесты для клиента
2. Развернуть приложение в докер контейнере.
3. Написать github actions для автотестов.
Критерии оценки:
1. Чистая архитектура/чистый код
2. Нейминг
3. Отсутсвие глобальных переменных
4. Умение использовать ООП
Ссылку на гитхаб, а так же любые вопросы присылайте в тг:
https://t.me/dev_lerk

### Для запуска проекта:

1) Склонируйте репозиторий:
``
https://github.com/ArtyomBatmanov/test_task_mera_capital.git
``
2) Запустите Docker контейнер
``
docker compose build
docker compose up
``
3) Описание endpoint'ов
- GET /prices - получение всех цен заданного тикера
- GET /prices/range - получение цен заданного тикера за определённый промежуток времени
- GET /prices/latest - получение последней цены заданного тикера