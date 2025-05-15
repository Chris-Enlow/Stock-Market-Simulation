from Stock import *
from Market import *
import yfinance as yf
import random

def get_random_ticker_list(n):
    with open("tickers.txt", "r") as file:
        tickers = [line.strip().upper() for line in file if line.strip()]
    
    selected_tickers = random.sample(tickers, n)    
    print(f"[DEBUG] Total stocks created: {len(selected_tickers)}")
    return selected_tickers


def main():
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
        print("Press V to view a list of stocks\nType a ticker to view its graph\nType 'continue' to go to the next day\n"
            "Type 'exit' to close market simulation\n")
        while(not advance):
            command = input("")
            if(command == "V"):
                for n in market.stocks:
                    print(n.name)
            elif(command == "continue"):
                advance = True
            elif(command == "exit"):
                exit()
            else:
                found = False
                for n in market.stocks:
                    if n.name == command:
                        n.draw()
                        found = True
                if not found:
                    print("Ticker not in current market.")
    

if __name__ == "__main__":
    main()