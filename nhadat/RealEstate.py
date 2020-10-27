from Trading import Trading

class RealEstate(Trading):
    def __init__(self, trading_code, trading_day,price, type_of_trade, square):
        self.trading_code = str(trading_code)
        self.trading_day = trading_day
        self.price = price
        self.type = str(type_of_trade)
        self.square = square


    def getPriceWithoutVAT(self):
        if self.type == 0:
            paid =self.price = self.square * self.price
            return paid
        paid = self.price = self.square * self.price * 2.0
        return paid

    def getPriceWithVAT(self):
        if self.type == 0:
            paid = self.square * self.price +( self.square * self.price )*0.1
            return paid
        paid = self.square * self.price * 2.0 + ( self.square * self.price * 2.0)*0.1
        return paid
    
    def setData(self):
        trading_code = str(input("type your trading code here: "))
        trading_day = str(input("type your trading day here (ex: 11/10/2020): "))
        price = input("Type the price: ")
        type_of_trade = input("Type your type of trade btw A(0) and B(1) :")
        square = input("Type square: ")
        self.trading_code = str(trading_code)
        self.trading_day = trading_day
        self.price = price
        self.type = str(type_of_trade)
        self.square = square
    
