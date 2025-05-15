import random
import matplotlib.pyplot as plt

class Stock:

    def __init__(self, name):
        self.name = name
        self.xPOIs = []
        self.yPOIs = []
        self.xPOIs.append(0)
        self.yPOIs.append(0)

    def printName(self):
        print(self.name)

    def draw(self):
        plt.cla()
        plt.plot(self.xPOIs, self.yPOIs)
        plt.title(self.name)
        plt.show()

    def addPOI(self, x, y):
        self.xPOIs.append(x)
        self.yPOIs.append(y)

    def updateStock(self, day):
        increment = 5
        decrement = 5
        currentPrice = self.yPOIs[day-1]
        if (currentPrice < decrement):
            decrement = currentPrice
        num = random.randint(currentPrice - decrement, currentPrice + increment)
        print(num)
        self.addPOI(day, num)
