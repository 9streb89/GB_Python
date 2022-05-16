import requests
import datetime


def currency_rates(val):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    result = requests.get(url)
    res = str(result.text)
    index_start = res.find('<Value>', res.find(val))
    index_end = res.find('</Value>', res.find(val))
    dt = str(res[60:70])
    dtd = datetime.datetime.strptime(dt, '%d.%m.%Y').strftime('%Y-%m-%d')
    return (res[index_start + 7: index_end], (dtd))



# print(currency_rates('USD'))
# print(currency_rates('EUR'))

