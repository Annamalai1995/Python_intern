class Deal:
    __seller=""  #private variables
    __buyer=""
    __value=0
    def __init__(self,s="",b="",v=0):
        print("Deal called")
        self.__seller=s
        self.__buyer=b
        self.__value=v
    def __str__(self):return self.__seller+" "+self.__buyer+" "+str(self.__value)+"\n"
    def setSeller(self,sel):
        self.__seller=sel
    def getSeller(self):
        return self.__seller
    def setBuyer(self,buy):
        self.__buyer=buy
    def getBuyer(self):
        return self.__buyer
    def setValue(self,val):
        self.__value=val
    def getValue(self):
        return self.__value

d1=Deal()
d1.setSeller("hiruthick")
d1.setBuyer("Roshini")
d1.setValue(150000)
print(d1.getSeller(),d1.getBuyer(),d1.getValue())
d2=Deal("Annamalai","sam",1450000)
print(d2)
