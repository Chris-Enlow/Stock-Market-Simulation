class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.stocks = {}

    def buyStock(self, stock, quantity):
        cost = stock.price * quantity
        if cost > self.balance:
            print(f"Not enough balance to buy {quantity} shares of {stock.name}.")
            return
        
        self.balance -= cost
        if stock.name in self.stocks:
            self.stocks[stock.name] = (stock, self.stocks[stock.name][1] + quantity)
        else:
            self.stocks[stock.name] = (stock, quantity)
        print(f"Bought {quantity} shares of {stock.name} at ${stock.price} each. Remaining balance: ${self.balance:.2f}")

    def sellStock(self, stock, quantity):
        if stock.name not in self.stocks:
            print(f"You do not own any shares of {stock.name}.")
            return
        owned_quantity = self.stocks[stock.name][1]
        if quantity > owned_quantity:
            print(f"Not enough shares to sell. You own {owned_quantity} shares of {stock.name}.")
            return
        self.balance += stock.price * quantity
        if quantity == owned_quantity:
            del self.stocks[stock.name]
        else:
            self.stocks[stock.name] = (stock, owned_quantity - quantity)
        print(f"Sold {quantity} shares of {stock.name} at ${stock.price} each. New balance: ${self.balance:.2f}")

    def viewPortfolio(self):
        print(f"\n--- Portfolio for {self.owner} ---")
        print(f"Balance: ${self.balance:.2f}")
        if not self.stocks:
            print("No stocks owned.")
            return
        for ticker, (stock, quantity) in self.stocks.items():
            print(f"{ticker}: {quantity} shares @ ${stock.price} each (Total: ${stock.price * quantity:.2f})")
        print("-----------------------------\n")
