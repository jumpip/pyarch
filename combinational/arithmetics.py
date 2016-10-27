import gates
import sys
sys.path.insert(0, '../utils')
import new
sys.path.insert(0, '../connectors')
import transport

class HalfAdder(new.Hardware,object):
     def __init__(self,x,s):
                try:
                        (len(x) != 2 or len(s) != 2)
                except NotImplementedError:
                        print('Invalid Connections')
                input=[]
                input.append(x)
                self.input=input
                self.output=s
                super(HalfAdder,self).__init__([x, s])
                self.components.append(gates.XorGate([x[0]],[x[1]],[s[1]]))
                self.components.append(gates.AndGate([x[0]],[x[1]],[s[0]]))

class FullAdder(new.Hardware,object):
    def __init__(self,x,s):
        try:
            (len(x)!=3 or len(s)!=2)
        except NotImplementedError:
            print('Invalid Connections')
        super(FullAdder,self).__init__([x,s])
        input=[]
        input.append(x)
        self.input=input
        self.output=s
        self.internalWiring = transport.wires(3)
        self.components.append(HalfAdder([x[0],x[1]],[self.internalWiring[0], self.internalWiring[1]]))
        self.components.append(HalfAdder([self.internalWiring[1],x[2]],[self.internalWiring[2],s[1]]))
        self.components.append(gates.OrGate([self.internalWiring[0]],[self.internalWiring[2]],[s[0]]))

class PipoAdder(new.Hardware,object):

    def __init__(self,x,y,s):
        try:
            (len(x) != len(y) or len(s) != len(x)+1)
        except NotImplementedError:
            print('Invalid Connections')
        super(PipoAdder,self).__init__([x,y,s])
        input = []
        input.append(x)
        input.append(y)
        self.input=input
        self.output=s
        size = len(x)
        self.internalWiring = transport.wires(size)
        if size > 1:
            self.components.append(FullAdder([x[0], y[0], self.internalWiring[0]], [self.internalWiring[1], s[size]]))
            for i in xrange(size-1):
                self.components.append(FullAdder([x[i], y[i], self.internalWiring[i]], [self.internalWiring[i+1], s[size-i]]))
            self.components.append(FullAdder([x[size-1], y[size-1], self.internalWiring[size-1]], [s[0], s[1]]))
        else:
            self.components.append(FullAdder([x[0], y[0], self.internalWiring[0]], [s[0], s[1]]))
        self.internalWiring[0].propagateSignal(0)
