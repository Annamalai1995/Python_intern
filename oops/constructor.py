class Car:
    def __init__(self, brand,name):
        self.brand = brand
        self.name = name

    def display(self):
        print(f"Brand: {self.brand}, NAME: {self.name}")

C= Car("Maruthi","Swift")
c1=Car("Benz",'c class')
C.display()
c1.display()
