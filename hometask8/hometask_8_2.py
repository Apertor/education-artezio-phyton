"""hometask 8.2"""
# Напишите функцию, которая принимает три аргумента
#   1)число, количество денег в исходной валюте, float;
#   2)исходная валюта, трехсимвольная строка, str;
#   3)целевая валюта, трехсимвольная строка, str;
#   и возвращает количество денег в целевой валюте (тип float).
#   Для получения курса валют воспользуйтесь https://api.exchangerate-api.com .

import requests


def get_currency_course(source_currency):
    """get currency course"""
    url_currency = 'https://api.exchangerate-api.com/v4/latest/'+source_currency
    r = requests.get(url_currency)
    return r.text


def exchange_rate(amount, cur_symbol_1, cur_symbol_2):
    """exchange_rate(1, "USD", "RUB") --> 63.54518 (for 2020.02.17)"""
    message = get_currency_course(cur_symbol_1)
    s = message[message.find(cur_symbol_2):]
    course = float(s[s.find(":") + 1:s.find(",")])
    return amount*course


print(exchange_rate(1, "USD", "RUB"))
print(exchange_rate(1000, "EUR", "RUB"))
print(exchange_rate(1000, "GBP", "RUB"))
