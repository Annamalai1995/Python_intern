from abc import ABC
class bus(ABC):
    def volvo(self):
        print("Hello")
        print("YYY")
        
class SRT(bus):
    def volvo(self):
        print("It a luxary bus")
class KPN(bus):
    def A(self):
        print("AC BUS ")
class SAT(bus):
    def volvo(self):
        print("Luxary vehicle ")
s=SRT()
s.volvo()
s1=SAT()
s1.volvo()
b=bus()
b.volvo() 
# s=SAT()
# s.volvo()
# s.volvo()
# A=ABC()
# A.volvo()