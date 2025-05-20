class Market:
    stocks = []
    day = 1

    def __init__(self, stocks):
        self.stocks = stocks

    def marketUpdate(self):
        for x in self.stocks:
            x.updateStock(self.day)
        self.day += 1
    
    def getStock(self, ticker):
        for x in self.stocks:
            if x.name == ticker:
                return x
        return "No Such Stock"
