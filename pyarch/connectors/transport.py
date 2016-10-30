import sys
sys.path.insert(0, '../utils')
import ioManager
import new
import threading
from functools import partial
from pyee import EventEmitter
from hiatus import set_interval,clear_interval


def wires(number):
    wireSet = list()
    for i in xrange(0,number):
        wireSet.append(Wire(None))
    return wireSet

class Wire(EventEmitter,object):

    def propagateSignal(self,newSig):
        oldSig = self.signal
        self.signal = newSig
        if(oldSig != self.signal):
            self.emit('signal')

    def getSignal(self):
        return self.signal

    def __init__(self,sig):
        super(Wire,self).__init__()
        self.signal = sig

class Pulse(Wire,object):

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

    def __init__(self,time,val):
        super(Pulse,self).__init__()
        self.val = val
        self.timePeriod = time
        self.interval = None
