# this module is for defining a class called "equipment" and initializing members of that class
from Steve_functions import timestamp, duration
#from SQL_Interface import *

class Tool:
    def __init__(self, Name, Description, Manufacturer, RetailPrice, PurchasePrice, Vendor, PurchaseDate):
        self.Name = Name
        self.Description = Description
        self.Manufacturer = Manufacturer
        self.RetailPrice = RetailPrice
        self.PurchasePrice = PurchasePrice
        self.Vendor = Vendor
        self.PurchaseDate = PurchaseDate

class Equipment:                                                #class for equipment that we want to monitor
    def __init__(self, name, state, onTime, offTime, runTime):  #method to buil object attributes
        self.name = name
        self.state = state
        self.onTime = onTime
        self.offTime = offTime
        self.runTime = runTime

    def on(self):                                               #method to run when equipment is turned on
        self.onTime = timestamp()                               #provides a timestamp of when the equipment was turned on
        print("The sump pump turned on at ", end="")
        print(self.onTime)

    def off(self):                                              #method to run when equipment is turned off
        self.offTime = timestamp()                              #provides a timestamp of when the equipment was turned off
        self.runTime = duration(self.onTime, self.offTime)      #calls duration function to record how long the pump ran for
        print("The sump pump turned off at ", end="")
        print(self.offTime, end="")
        print(" and ran for ", end="")
        print(self.runTime)

    def record(self):                                           #method for recording data about equipment run sessions
        if self == sumpPump:                                    #probably a better way of doing this, by passing self to a genaric record function
            sump_pump_record(self)


sumpPump = Equipment("Sump Pump", False, timestamp(), timestamp(), timestamp()) #initializes an instance of the equipment class