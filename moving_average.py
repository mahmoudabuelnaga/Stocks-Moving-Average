import requests
from datetime import timedelta
import datetime
import csv


class SMA:
    def __init__(self):
        self.n = int(input('Please enter The number of days to which the moving average calculation is applied? '))
        self.ticker = input('Please enter the stock symbol identifier? ')
        self.__apiKey = "NbQISUEZb_uhgZjdGJSccratppL3EDNh"
    
    def get_date(self):
        date = datetime.date(2021, 12, 31) - timedelta(days=self.n)
        return date
    

    def stocks_moving_average(self):
        endpoints = f"https://api.polygon.io/v2/aggs/ticker/{self.ticker}/range/1/day/{self.get_date()}/2021-12-31?sort=asc&apiKey={self.__apiKey}"
        
        get_response = requests.get(endpoints)

        results = get_response.json()
        
        queryCount = results['queryCount']

        ticker = results['ticker']

        number_of_days = self.n

        from_date = self.get_date()

        to = datetime.date(2021, 12, 31)
        
        closing_prices = 0
        
        for i in results['results']:
            closing_prices += i['c']

        sma = closing_prices/queryCount
        return {'ticker': ticker,'number_of_days': number_of_days,'from_date': from_date,'to': to,'sma': sma, }


    def export_file_csv(self):
        filename = f'sma-{datetime.datetime.today()}.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Ticker','number_of_days','from','to', 'SMA'])
            writer.writerow([
                    self.stocks_moving_average()['ticker'], 
                    self.stocks_moving_average()['number_of_days'], 
                    self.stocks_moving_average()['from_date'],
                    self.stocks_moving_average()['to'],
                    self.stocks_moving_average()['sma'],
                ])


if __name__ == "__main__":
    sma = SMA()
    sma.export_file_csv()
