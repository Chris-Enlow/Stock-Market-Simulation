from Stock import *
from Market import *
from Account import *
import yfinance as yf
import random

def get_random_ticker_list(n):
    with open("../tickers.txt", "r") as file:
        tickers = [line.strip().upper() for line in file if line.strip()]
    
    selected_tickers = random.sample(tickers, n)    
    return selected_tickers


def main():
    accountDetails = input("Type in a name and a starting balance to begin\nex: \"Chris 1000\"")
    username, startBalance = accountDetails.split()
    account = Account(username, int(startBalance))
    num_stocks = random.randint(5, 10)
    tickerList = get_random_ticker_list(num_stocks)
    stockList = []
    for ticker in tickerList:
        stock = Stock(ticker)
        stockList.append(stock)
    market = Market(stockList)
    days = 10
    print(len(stockList))
    for x in range(0, days):
        market.marketUpdate()
        advance = False
        print("Type 'view market' to view a list of stocks\nType a ticker to view its graph\nType 'continue' to go to the next day\n"
            "Type 'exit' to close market simulation\n")
        
        while(not advance):
            command = input("")
            if(command == "view market"):
                for n in market.stocks:
                    print(n.name)
            elif command.startswith("buy "):
                _, ticker, qty = command.split()
                qty = int(qty)
                stock = market.getStock(ticker)
                if isinstance(stock, Stock):
                    account.buyStock(stock, qty)
                else:
                    print("Ticker not in current market.")

            elif command.startswith("sell "):
                _, ticker, qty = command.split()
                qty = int(qty)
                stock = market.getStock(ticker)
                if isinstance(stock, Stock):
                    account.sellStock(stock, qty)
                else:
                    print("Ticker not in current market.")

            elif command == "portfolio":
                account.viewPortfolio()
            elif(command == "continue"):
                advance = True
            elif(command == "exit"):
                exit()
            elif(command.startswith("view ")):
                _, ticker = command.split()
                found = False
                for n in market.stocks:
                    if n.name == ticker:
                        n.draw()
                        found = True
                if not found:
                    print("Ticker not in current market.")
    

if __name__ == "__main__":
    main()