import sys
sys.path.insert(0, '../utils')
import ioManager
import new

class AndGate(new.Hardware):

        def __init(self,x,y,o):
                try:
                        (len(x) != 1 or len(y) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(AndGate,self).__init__([x, y, o])
                self.x = x
                self.y = y
                self.o = o
                #event handling fixes needed
                hardware = partial(hardware, self)

        def hardware():
                xSig = self.x[0].getSignal()
                ySig = self.y[0].getSignal()
                try:
                        xSig, ySig
                except NameError:
                        self.o[0].propagateSignal(undefined)
                if(xSig == 0 or ySig == 0):
                        self.o[0].propagateSignal(0)
                else:
                        self.o[0].propagateSignal(xSig and ySig)

class OrGate(new.Hardware):

        def __init(self,x,y,z,o):
                try:
                        (len(x) != 1 or len(y) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(OrGate,self).__init__([x, y, o])
                self.x = x
                self.y = y
                self.o = o
                #event handling fixes needed
                hardware = partial(hardware, self)

        def hardware():
                xSig = self.x[0].getSignal()
                ySig = self.y[0].getSignal()
                try:
                        xSig, ySig
                except NameError:
                        self.o[0].propagateSignal(undefined)
                if(xSig == 1 or ySig == 1):
                        self.o[0].propagateSignal(1)
                else:
                        self.o[0].propagateSignal(xSig or ySig)

class NotGate(new.Hardware):

        def __init(self,x,o):
                try:
                        (len(x) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(NotGate,self).__init__([x, o])
                self.x = x
                self.o = o
                #event handling fixes needed
                hardware = partial(hardware, self)

        def hardware():
                xSig = self.x[0].getSignal()
                try:
                        xSig
                except NameError:
                        self.o[0].propagateSignal(undefined)
                if(xSig == 1):
                        self.o[0].propagateSignal(0)
                else:
                        self.o[0].propagateSignal(1)


