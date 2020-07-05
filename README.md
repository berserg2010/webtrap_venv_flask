## Запуск приложения

Запустить можно так:

    flask run
    
или, добавив права на исполнение, так:
    
    ./manage.py
    
Можно укажать порт таким способом:
    
    PORT=8008 flask run

или:
    
    PORT=8008 ./manage.py

Порт поумолчанию `8888`.

## Тесты

Запуск тестов:

    python3 -m pytest
