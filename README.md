# Установка
Ловите парсер, который не только даёт вам IP и PORT [с бесплатного сайта](spys.one/proxies "spys.one"), но еще и проверяет каждый прокси на работуспособность!
* Открываем терминал/cmd и скачиваем репозиторий:
* ```git clone https://github.com/eXTrimeXT/Parser_spys.git``` 
* Устанавливаем все требования: 
* ```cd Parser_spys```
* ```python3 -m pip install -r requirements.txt```
* Запускаем парсер: 
* ```python3 parser_spys_proxy.py```
* Открываем файл ```MyProxy.txt``` и видим, какие прокси пригодны для использования.
# Возможные ошибки
* Если вы используете не Google Chrome v88, то [скачайте драйвер для своего браузера!](https://selenium-python.readthedocs.io/installation.html "Скачать веб-драйвер")
* Откройте файл ```parser_spys_proxy.py``` и отредактируйте строку
* ```pathWebDriver = "./Chrome88"```
* Замените ```Chrome88``` на имя своего драйвера, который должен быть в этой же папке или вы должны указать путь полностью!
