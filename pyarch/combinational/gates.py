import sys
sys.path.insert(0, '../utils')
import ioManager
import new
from functools import partial

class AndGate(new.Hardware,object):

        def __init__(self,x,y,o):
                try:
                        (len(x) != 1 or len(y) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(AndGate,self).__init__([x,y,o])
                input=[]
                input.append(x)
                input.append(y)
                self.input=input
                self.output=o
                self.x = x
                self.y = y
                self.o = o
                x[0].on('signal', self.hardware)
                y[0].on('signal', self.hardware)

        def hardware(self):
                xSig = self.x[0].getSignal()
                ySig = self.y[0].getSignal()
                try:
                        xSig, ySig
                except NameError:
                        self.o[0].propagateSignal(None)
                if(xSig == 0 or ySig == 0):
                        self.o[0].propagateSignal(0)
                else:
                        self.o[0].propagateSignal(1)

class NandGate(new.Hardware,object):

        def __init__(self,x,y,o):
                try:
                        (len(x) != 1 or len(y) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(NandGate,self).__init__([x,y,o])
                input=[]
                input.append(x)
                input.append(y)
                self.input=input
                self.output=o
                self.x = x
                self.y = y
                self.o = o
                x[0].on('signal', self.hardware)
                y[0].on('signal', self.hardware)
               
        def hardware(self):
                xSig = self.x[0].getSignal()
                ySig = self.y[0].getSignal()
                try:
                        xSig, ySig
                except NameError:
                        self.o[0].propagateSignal(None)
                if(xSig == 0 or ySig == 0):
                        self.o[0].propagateSignal(1)
                else:
                        self.o[0].propagateSignal(0)

class OrGate(new.Hardware,object):

        def __init__(self,x,y,o):
                try:
                        (len(x) != 1 or len(y) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(OrGate,self).__init__([x, y, o])
                input=[]
                input.append(x)
                input.append(y)
                self.input=input
                self.output=o
                self.x = x
                self.y = y
                self.o = o
                x[0].on('signal', self.hardware)
                y[0].on('signal', self.hardware)
                hardware = partial(self.hardware, self)

        def hardware(self):
                xSig = self.x[0].getSignal()
                ySig = self.y[0].getSignal()
                try:
                        xSig, ySig
                except NameError:
                        self.o[0].propagateSignal(None)
                if(xSig == 1 or ySig == 1):
                        self.o[0].propagateSignal(1)
                else:
                        self.o[0].propagateSignal(0)

class NorGate(new.Hardware,object):

        def __init__(self,x,y,o):
                try:
                        (len(x) != 1 or len(y) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(NorGate,self).__init__([x, y, o])
                input=[]
                input.append(x)
                input.append(y)
                self.input=input
                self.output=o
                self.x = x
                self.y = y
                self.o = o
                x[0].on('signal', self.hardware)
                y[0].on('signal', self.hardware)
                
        def hardware(self):
                xSig = self.x[0].getSignal()
                ySig = self.y[0].getSignal()
                try:
                        xSig, ySig
                except NameError:
                        self.o[0].propagateSignal(None)
                if(xSig == 1 or ySig == 1):
                        self.o[0].propagateSignal(0)
                else:
                        self.o[0].propagateSignal(1)


class NotGate(new.Hardware,object):

        def __init__(self,x,o):
                try:
                        (len(x) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(NotGate,self).__init__([x, o])
                input=[]
                input.append(x)
                self.input=input
                self.output=o
                self.x = x
                self.o = o
                x[0].on('signal', self.hardware)

        def hardware(self):
                xSig = self.x[0].getSignal()
                try:
                        xSig
                except NameError:
                        self.o[0].propagateSignal(undefined)
                if(xSig == 1):
                        self.o[0].propagateSignal(0)
                else:
                        self.o[0].propagateSignal(1)

class XorGate(new.Hardware,object):

        def __init__(self,x,y,o):
                try:
                        (len(x) != 1 or len(y) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(XorGate,self).__init__([x, y, o])
                input=[]
                input.append(x)
                input.append(y)
                self.input=input
                self.output=o
                self.x = x
                self.y = y
                self.o = o
                x[0].on('signal', self.hardware)
                y[0].on('signal', self.hardware)

        def hardware(self):
                xSig = self.x[0].getSignal()
                ySig = self.y[0].getSignal()
                try:
                        xSig, ySig
                except NameError:
                        self.o[0].propagateSignal(undefined)
                if(xSig != ySig):
                        self.o[0].propagateSignal(1)
                else:
                        self.o[0].propagateSignal(0)
