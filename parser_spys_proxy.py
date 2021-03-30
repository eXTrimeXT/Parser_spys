from selenium import webdriver
from selenium.webdriver.support.ui import Select
from colorama import init, Fore, Style
import requests
import time
import os

# Install all requirements!
# python3 -m pip install -r requirements_for_parser.txt 

init()  # colorama

# путь до драйвера
pathWebDriver = "./Chrome88"
options = webdriver.ChromeOptions()  # настройки для браузера
options.add_argument('headless')  # для открытия headless-браузера(без окна)
# Чтобы запустить графический режим уберите: chrome_options=options
browser = webdriver.Chrome(executable_path = pathWebDriver, chrome_options=options)
os.system("clear")  # Очищаем терминал/CMD-привет Шиндузятник :D
# Общая переменная xpath
xpath = "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr["
# Массив со всеми IP:PORT
list_proxy = []
# Hardcode fixes:
opening_site = "** Открываем сайт **"
site_url = "https://spys.one/proxies/"
page_title = "Бесплатные HTTP, HTTPS, SOCKS прокси сервера, списки обновляемых IP адресов проксей онлайн"
no_results = "No results found."
page_error_msg = "Вы не попали на страницу!"
setting_filters = "** Настраиваем фильтры **"
parsing_msg = "*** Парсим прокси ***\n"
checking_msg = "\n*** Проверяем прокси ***\n"
test_site_url = "https://www.google.com/"
console_logo = """
    ____  ____  ____ _  ____  __
   / __ \/ __ \/ __ \ |/ /\ \/ /
  / /_/ / /_/ / / / /   /  \  / 
 / ____/ _, _/ /_/ /   |   / /  
/_/   /_/ |_|\____/_/|_|  /_/ 
       _  ________     _              
  ___ | |/ /_  __/____(_)___ ___  ___ 
 / _ \|   / / / / ___/ / __ `__ \/ _ \\\
 
/  __/   | / / / /  / / / / / / /  __/
\___/_/|_|/_/ /_/  /_/_/ /_/ /_/\___/ 
"""
no_headless = "The end. Press key..."

# открываем сайт
def openUrl():
	print(Fore.YELLOW + opening_site)
	browser.implicitly_wait(10)
	browser.implicitly_wait(10)
	browser.get(site_url)  # переходим на сайт
	# проверяем наличие того, что мы попали на страницу
	try:
		assert page_title in browser.title
		assert no_results not in browser.page_source  # мы не попали на страницу :(
	except:
		print(Fore.RED + page_error_msg + Fore.YELLOW)
		exit()
	browser.implicitly_wait(10)


def setFilters(number):
	print(setting_filters)
	# Можно добавить if/elif/else, чтобы можно было выбирать вид протокола
	type_http = Select(browser.find_element_by_xpath(f"{xpath}1]/td[2]/font/select[6]"))
	type_http.select_by_value("1")  # 0=Все 1=HTTP 2=SOCKS- протокол связи HTTP
	# Можно добавить if/elif/else чтобы можно было выбирать степень анонимности, но меня интересует 3 и 4
	# Думаю, что люди ищют прокси, чтобы быть анонимными, а иначе ЗАЧЕМ ?
	ANM = Select(browser.find_element_by_xpath(f"{xpath}1]/td[2]/font/select[3]"))
	ANM.select_by_value(str(number))  # 3=ANM - анонимный, 4=HIA - высокоанонимный тип прокси
	amount_proxy = Select(browser.find_element_by_xpath(f"{xpath}1]/td[2]/font/select[1]"))
	# Можно добавить if/elif/else, чтобы из выбирать кол-во прокси из параметра функции, но мне лень)
	amount_proxy.select_by_value("3")  # 0=25 1=50 2=100 3=200 4=300 5=500 


def parseProxy():
	print(Fore.RED + parsing_msg + Fore.YELLOW)
	for i in range(4, 204):  # 4, 204
		browser.implicitly_wait(10)
		address = str(browser.find_element_by_xpath(f"{xpath}{i}]/td[1]/font").text)
		print(f"IP[{i-3}] >> {address} ")
		list_proxy.append(address)


def checkProxy(timeout):
	print(Fore.RED + checking_msg + Fore.YELLOW)
	for i in range(0, 200):  # 200 потому, что amount_proxy.select_by_value("3")
		proxy = list_proxy[i]
		request = requests.get(test_site_url, proxies={"http": proxy}, timeout=timeout)
		print(f"[{i+1}/200]Проверка (" + Fore.RED + f"{proxy}" + Fore.YELLOW + ") | Статус код -->> " + Fore.GREEN + f"{request.status_code}" + Fore.YELLOW)
		writeProxy(proxy, request.status_code, "MyProxy.txt")


def writeProxy(proxy, status_code, fileName: str):
	if int(status_code) == 200:
		f = open(fileName, "a")
		f.write(f"{proxy}\n")
		f.close()
		print("Прокси " + Fore.GREEN + f"{proxy}" + Fore.YELLOW + " был записан в файл " + Fore.GREEN + f"{fileName}" + Fore.YELLOW + " со статус кодом = " + Fore.GREEN + f"{status_code}" + Fore.YELLOW)

# Чисто для красоты, хочу чтобы глазу было приятно :D
def console_picture():
    print(Style.BRIGHT + Fore.GREEN)
    print(console_logo)
    print(Fore.YELLOW)
    time.sleep(0.5)    


console_picture()
openUrl()
for i in range(3, 5):
	setFilters(i)  # 3 и 4 т.к. число 5 считается как выколотая точка! Учи Python3 блин!
	parseProxy()
	checkProxy(10)
	list_proxy = []


input(no_headless)  # нужно для окна(NO headless), чтобы оно не закрывалось!
browser.close()  # закрываем драйвер
