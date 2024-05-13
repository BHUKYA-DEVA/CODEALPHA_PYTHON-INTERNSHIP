import requests

class Stock:
    def __init__(self, symbol, quantity):
        self.symbol = symbol
        self.quantity = quantity
        self.price = 0.0
        self.value = 0.0

    def update_price(self):
        api_key = 'ALPHA_VANTAGE_API_KEY'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if 'Global Quote' in data:
            self.price = float(data['Global Quote']['05. price'])
            self.value = self.price * self.quantity
        else:
            print(f"Failed to fetch data for {self.symbol}")

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, symbol, quantity):
        self.stocks.append(Stock(symbol, quantity))

    def update_prices(self):
        for stock in self.stocks:
            stock.update_price()

    def total_value(self):
        return sum(stock.value for stock in self.stocks)
if __name__ == "__main__":
    portfolio = Portfolio()

    portfolio.add_stock('AAPL', 10)
    portfolio.add_stock('MSFT', 5)
    portfolio.add_stock('GOOGL', 3)
    
    portfolio.update_prices()
    
    print("Portfolio Value:", portfolio.total_value())
