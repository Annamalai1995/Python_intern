class bike:
    def gear(self):
        print("5 speed gear box")
class car(bike):
    def benz(self):
        print("IS the classic  car")
c=car() #object creation
c.benz()
c.gear() 