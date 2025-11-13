class phone:
    def call(self):
        print("Making a call")
class Smartphone(phone):
    def browse(self):
        print("Browsing internet")
sp = Smartphone()
sp.call()
sp.browse()

#single level inheritance:-
class Bank:
    def openAccount(self):
        print("Account opened")

class HdfcBank(Bank):
    def rateOfInterest(self):
        print("HDFC Rate of Interest is 7%")
h = HdfcBank()
h.openAccount()   
h.rateOfInterest()    
