import requests as rq

def get_dict_rates():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = rq.get(url)
    valutes_dict = response.json()
    return valutes_dict['Valute']

