"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в
обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную
задачу? Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с
денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в
качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не
зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных
лучше использовать в ответе функции?
"""


import requests as rq
from bs4 import BeautifulSoup


def currency_rates(requests):
    """
    Я не уверен, что четко понял задание... Но! Моя функция принимает код валюты и возвращает цену в рублях и дату.
    Саму цену она берет с линки ниже. Сделано с костылями)
    """
    response = rq.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    soup = BeautifulSoup(response, 'lxml')
    block_date = soup.find('valcurs')
    date = str(block_date)[15:25]

    if requests == 'usd':
        block_usd = soup.find('valute', id="R01235")
        check_usd = block_usd.find_all('value')
        check_list_usd = str(check_usd)
        USD = check_list_usd[8:15]
        answer = USD
    elif requests == 'eur':
        block_eur = soup.find('valute', id="R01239")
        check_eur = block_eur.find_all('value')
        check_list_eur = str(check_eur)
        EUR = check_list_eur[8:15]
        answer = EUR
    elif requests == 'gbp':
        block_gbp = soup.find('valute', id="R01035")
        check_gbp = block_gbp.find_all('value')
        check_list_gbp = str(check_gbp)
        GBP = check_list_gbp[8:16]
        answer = GBP
    else:
        return None
    return f'На {date} курс {requests.upper()} = {answer} руб.'


requests = input("Пожалуйста, введите валюту курс которой вы бы хотели узнать (Прим: USD, EUR, GBP): ")
requests = requests.lower()
print(currency_rates(requests))
