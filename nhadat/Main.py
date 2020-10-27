from HouseTrading import HouseTrading
from RealEstate import RealEstate


def Main():

    def WriteDateIntoList(typeOfTrading):
        tradingList =[]
        if typeOfTrading == 0:
            tradingCode = str(input("type your trading code here: "))
            while tradingCode!="":
                trade = RealEstate(tradingCode,tradingDay,price,typeOfTrade,square)
                tradingList.append(trade)
        elif typeOfTrading==1:
            tradingCode = str(input("type your trading code here: "))
            while tradingCode!="" :
                trade = HouseTrading(tradingCode,tradingDay,price,typeOfTrade,square)
                tradingList.append(trade)


    userTypeOfTrade = input("choose your type of trade btw realestate(0) and housetrading(1): ")
    WriteDateIntoList(int(userTypeOfTrade))

if __name__ == "__main__":
    Main()