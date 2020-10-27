from abc import ABC, abstractclassmethod

# from Date import Date
import os
os.system("python Date.py")
class Trading(ABC):
    @abstractclassmethod
    def getPriceWithoutVAT(self):
        pass
    
    def getPriceWithVAT(self):
        pass


