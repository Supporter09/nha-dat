from Trading import Trading

class HouseTrading(Trading):
    def __init__(self, tradingCode, tradingDay,price, typeOfHouse, square,houseIndex):
        self.tradingCode = str(tradingCode)
        self.tradingDay = tradingDay
        self.price = price
        self.type = str(typeOfHouse)
        self.square = square
        self.houseIndex = houseIndex


    def getPriceWithoutVAT(self):
        if self.type ==0:
            paid =self.price = self.square * self.price * self.houseIndex
            return paid
        paid = self.price = self.square * self.price * self.houseIndex *1.5
        return paid

    def getPriceWithVAT(self):
        if self.type == 0:
            paid = self.square * self.price * self.houseIndex +( self.square * self.price * self.houseIndex )*0.05
            return paid
        paid = self.square * self.price * self.houseIndex *1.5 + (self.square * self.price * self.houseIndex *1.5)*0.05
        return paid

    def setData(self):
        tradingDay = str(input("type your trading day here (ex: 11/10/2020): "))
        price = input("Type the price: ")
        typeOfHouse = input("Type your type of trade btw cao cap(0) va biet thu(1):")
        square = input("Type square: ")
        houseIndex = input("Type house index")
        self.tradingCode = str(tradingCode)
        self.tradingDay = tradingDay
        self.price = price
        self.type = str(typeOfHouse)
        self.square = square
        self.houseIndex = houseIndex

