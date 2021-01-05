import requests
from bs4 import BeautifulSoup
import datetime
import time
from multiprocessing import Pool

target = ['UNVR','BMRI','INDF','BBCA']

def get_price(target):
    times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    f = open('/test_yahoo.txt', 'a')
    url = f'https://finance.yahoo.com/quote/{target}.JK?p={target}.JK&.tsrc=fin-srch'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('div', attrs={'class':'D(ib) Mend(20px)'})[0].find('span').text
    print(prices, times, target)
    data = f"{prices}, {times},{target}"
    f.write(data)
    f.write('\n')
    f.close()
    return target, times, prices
while True:
    with Pool(len(target)) as p:
        p.map(get_price, target)
        time.sleep(60)
