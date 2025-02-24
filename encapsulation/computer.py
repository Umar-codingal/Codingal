class Computer:

    def __init__(self):
        self.__maxprice=900

    def sell(self):
        print(f"Selling Price:{self.__maxprice}")

    def setMax(self,price):
        self.__maxprice=price


c=Computer()
c.sell()

c.__maxprice=1000
c.sell()

c.setMax(1000)
c.sell()