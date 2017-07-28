class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None

    def setPin(self):
        if self.pin == None:
            return int(input("Enter the pin value for the gate "+self.getLabel()+": "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: Input pin is already assigned for gate " + self.getLabel())            

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None

    def setPinA(self):
        if self.pinA == None:
            return int(input("Enter the pinA value for the gate "+self.getLabel()+": "))
        else:
            return self.pinA.getFrom().getOutput()

    def setPinB(self):
        if self.pinB == None:
            return int(input("Enter the pinB value for the gate "+self.getLabel()+": "))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: No available input pins for gate " + self.getLabel())

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.setPinA()
        b = self.setPinB()
        if (a==1 and b==1):
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.setPinA()
        b = self.setPinB()
        if (a==1 or b==1):
            return 1
        else:
            return 0            

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.setPin()
        if a == 0:
            return 1
        elif a == 1:
            return 0

class Connector:
    def __init__(self,fgate,tgate):
        self.fromGate = fgate
        self.toGate = tgate

        tgate.setNextPin(self) #Set an input pin of the next gate to self

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate

def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()
