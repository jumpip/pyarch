import sys
sys.path.insert(0, '../utils')
import ioManager
import new
import threading
from pyee import EventEmitter
from hiatus import set_interval,clear_interval

def wires(number):
    wireSet = list()
    for i in xrange(0,number):
        wireSet.append(Wire())
    return wireSet

class Wire(EventEmitter):

    def __init__(self,sig):
        super(Wire,self)
        self.signal = sig
        self.propagateSignal = partial(propagateSignal,self)
        self.getSignal = partial(getSignal,self)

    def propagateSignal(self,newSig):
        oldSig = self.signal
        self.signal = newSig
        if(oldSig != self.signal):
            self.emit('signal')

    def getSignal():
        return self.signal

class Pulse(Wire):

    def __init__(self,time,val):
        super(Pulse,self)
        self.val = val
        self.timePeriod = time
        self.alter = partial(alter,self)
        self.switchOn = partial(switchOn,self)
        self.switchOff = partial(switchOff,self)
        self.interval = None

    def alter(self):
        self.propagateSignal(int(not self.signal))

    def switchOn(self):
        if(not self.interval):
            self.signal = self.val
            self.interval = set_interval(self.alter,self.timePeriod)

    def switchOff(self):
        if(self.interval):
            clear_interval(self.interval)
            self.signal = None
            self.interval = None
