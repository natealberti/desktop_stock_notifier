from win10toast import ToastNotifier
from bs4 import BeautifulSoup as soup
import requests

#stock functions#

# scrapes the daily percentage gain from robinhood to determine how well my stocks did today
def individual_stocks():
    return ['tsla',
            'arkf',
            'u',
            'tsm',
            'se',
            'nvda',
            'amd',
            'sq',
            'goog',
            'driv',
            'smh',]

def daily_return(stock):
    #connection to robinhood
    rh_endpoint = f'https://robinhood.com/stocks/{stock}'
    rh = requests.get(rh_endpoint).text
    bs = soup(rh, 'html.parser')
    raw_text = bs.find('div', class_='_27rSsse3BjeLj7Y1bhIE_9').find('span', class_='css-dq91k1').text
    #cleaning up text
    fixed = ''
    b = False
    for i in raw_text:
        if (i == '('):
            b = True
        if (b):
            fixed += i

    strs = fixed.replace('(', '').replace(')', '').replace('%', '')
    return strs

#avg return rate of my stocks
def RH_daily_report():
    returns = []
    num_of_stocks = len(individual_stocks())
    sum = 0
    for i in individual_stocks():
        returns.append(daily_return(i))
        add = float(daily_return(i))
        sum += add
    return sum/num_of_stocks

#percentage daily return of bitcoin today
def BTC_daily_report():
    # connection to robinhood
    rh_endpoint = 'https://robinhood.com/crypto/BTC'
    rh = requests.get(rh_endpoint).text
    bs = soup(rh, 'html.parser')
    raw_text = bs.find('div', class_='_27rSsse3BjeLj7Y1bhIE_9').find('span', class_='css-dq91k1').text
    # cleaning up text
    fixed = ''
    b = False
    for i in raw_text:
        if (i == '('):
            b = True
        if (b):
            fixed += i

    return fixed.replace('(', '').replace(')', '')

#creating icon for the notification
if __name__=='__main__':
    message = 'Stocks returned ' + str(RH_daily_report().__round__(2)) + '% today'
    toast = ToastNotifier()
    toast.show_toast(title='STOCKS report', msg=message, duration=5)