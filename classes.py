## Classes

class Stock: 
    def __init__(self, close, sector): 
        self.close = close
        self.sector = sector

aapl = Stock(100, 'tech')

print(aapl.sector)

