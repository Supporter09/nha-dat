from abc import ABC, abstractclassmethod

from abc import ABC, abstractclassmethod
# from Date import Date
import os
os.system("python Date.py")
class trading(ABC):
    @abstractclassmethod
    def getPriceWithoutVAT(self):
        pass
    
    def getPriceWithVAT(self):
        pass


class realEstate(trading):
    def __init__(self, tradingCode, tradingDay,price, typeOfTrade, square):
        self.__traingCode = str(tradingCode)
        self.__tradingDay = tradingDay
        self.__price = price
        self.__type = str(typeOfTrade)
        self.__square = square


    def getPriceWithoutVAT(self):
        if self.__type == "A":
            paid =self.__price = self.__square * self.__price
            return paid
        elif self.__type == "B":
            paid = self.__price = self.__square * self.__price * 2.0
            return paid

    def getPriceWithVAT(self):
        if self.__type == "A":
            paid = self.__square * self.__price +( self.__square * self.__price )*0.1
            return paid
        elif self.__type == "B":
            paid = self.__square * self.__price * 2.0 + ( self.__square * self.__price * 2.0)*0.1
            return paid

class houseTrading(trading):
    def __init__(self, tradingCode, tradingDay,price, typeOfHouse, square,houseIndex):
        self.__traingCode = str(tradingCode)
        self.__tradingDay = tradingDay
        self.__price = price
        self.__type = str(typeOfHouse)
        self.__square = square
        self.__houseIndex = houseIndex


    def getPriceWithoutVAT(self):
        if self.__type == "cao cap":
            paid =self.__price = self.__square * self.__price * self.__houseIndex
            return paid
        elif self.__type == "biet thu":
            paid = self.__price = self.__square * self.__price * self.__houseIndex *1.5
            return paid

    def getPriceWithVAT(self):
        if self.__type == "cao cap":
            paid = self.__square * self.__price * self.__houseIndex +( self.__square * self.__price * self.__houseIndex )*0.05
            return paid
        elif self.__type == "biet thu":
            paid = self.__square * self.__price * self.__houseIndex *1.5 + (self.__square * self.__price * self.__houseIndex *1.5)*0.05
            return paid

moi = realEstate("0101",[0,1,2000],1000,"A",100)
print("Tien ban phai tra khi khong co VAT la {}".format(moi.getPriceWithoutVAT()))
print("Tien ban phai tra khi co VAT la {}".format(moi.getPriceWithVAT()))

moi_nha = houseTrading("0101",[0,1,2000],1000,"A",100,3)
print("Tien ban phai tra khi khong co VAT la {}".format(moi_nha.getPriceWithoutVAT()))
print("Tien ban phai tra khi co VAT la {}".format(moi_nha.getPriceWithVAT()))

TradingCodeList = []
def WriteDateIntoList(typeOfTrading):
    tradingList =[]
    if typeOfTrading.lower() == "realestate":
        traingCode = str(input("type your trading code here: "))
        tradingDay = str(input("type your traing day here (ex: 11 10 2020): "))
        price = input("Type the price: ")
        typeOfTrade = str(input("Type your type of trade btw A and B :"))
        square = input("Type square: ")
        
        while traingCode!="":
            trade = realEstate(tradingCode,tradingDay,price,typeOfTrade,square)
            tradingList.append(trade)
    elif typeOfTrading.lower()=="housetrading":
        traingCode = str(input("type your trading code here: "))
        while traingCode!="" :
            tradingDay = str(input("type your traing day here (ex: 11 10 2020): "))
            price = input("Type the price: ")
            typeOfTrade = str(input("Type your type of trade btw cao cap va biet thu:"))
            square = input("Type square: ")
            houseIndex = input("Type house index")
            trade = houseTrading(tradingCode,tradingDay,price,typeOfTrade,square)
            tradingList.append(trade)


userTypeOfTrade = input("choose your type of trade btw realestate and housetrading: ")
WriteDateIntoList(userTypeOfTrade)