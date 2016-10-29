import sys
sys.path.insert(0, '../utils')
import new
sys.path.insert(0, '../combinational')
import gates
sys.path.insert(0, '../connectors')
import transport
from functools import partial

class SRFlipFlop(new.Hardware,object):

        def __init__(self,s,r,qqbar,c):
                try:
                        (len(s) != 1 or len(r) != 1 or len(qqbar) != 2)
                except NotImplementedError:
                        print('Invalid Connections')
                super(SRFlipFlop,self).__init__([s,r,[qqbar[0]]])
                input=[]
                input.append(s)
                input.append(r)
                input.append(c)
                self.input=input
                self.output=qqbar
                self.internalWiring = transport.wires(2)
                self.components.append(gates.AndGate(c,s,[self.internalWiring[0]]))
                self.components.append(gates.AndGate(c,r,[self.internalWiring[1]]))
                self.components.append(gates.NorGate([self.internalWiring[0]],[qqbar[0]],[qqbar[1]]))
                self.components.append(gates.NorGate([self.internalWiring[1]],[qqbar[1]],[qqbar[0]]))

class DFlipFlop(new.Hardware,object):

    def __init__(self,d,qqbar,c):
        try:
             len(d) !=1 or len(qqbar)!=2
        except NotImplementedError:
            print('Invalid Connections')
        super(DFlipFlop,self).__init__([d,qqbar[0]])
        input=[]
        input.append(d)
        input.append(c)
        self.input=input
        self.output=qqbar
        self.internalWiring = transport.wires(3)
        self.components.append(gates.NotGate(d, [self.internalWiring[0]]))
        self.components.append(gates.NandGate(c, d, [self.internalWiring[1]]))
        self.components.append(gates.NandGate(c, [self.internalWiring[0]], [self.internalWiring[2]]))
        self.components.append(gates.NorGate([self.internalWiring[1]], [qqbar[1]], [qqbar[0]]))
        self.components.append(gates.NorGate([self.internalWiring[2]], [qqbar[0]], [qqbar[1]]))
