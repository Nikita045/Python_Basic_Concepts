from OopsDemo import Calculator

class Child (Calculator):
    num2=200
    #creating child constructor and invoking parent constructor in it
    def __init__(self):
        Calculator.__init__(self,10,2)
    def getCompleteData(self):
        return self.num+self.num2+self.summation()

obj=Child()
print(obj.getCompleteData())

