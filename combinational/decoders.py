import gates
import sys
sys.path.insert(0, '../utils')
import new
sys.path.insert(0, '../connectors')
import transport

class Decoder1x2(new.Hardware,object):
     def __init__(self,x,o):
                try:
                        (len(x) != 1 or len(o) != 1)
                except NotImplementedError:
                        print('Invalid Connections')
                super(Decoder1x2,self).__init__([x,[o[0],x[0]]])
                self.components.append(gates.NotGate(x,o))

class Decoder2x4(new.Hardware,object):
    def __init__(self,x0,x1,o):
        try:
            (len(x0)!=1 or len(x1)!=1 or len(o)!=4)
        except NotImplementedError:
            print('Invalid Connections')
        super(Decoder2x4,self).__init__([x0,x1,o])
        input=[]
        input.append(x0)
        input.append(x1)
        self.input=input
        self.output=o
        self.internalWiring = wires(2)
        self.components.append(Decoder1x2(x0, [self.internalWiring[0]]))
        self.components.append(Decoder1x2(x1, [self.internalWiring[1]]))
        self.components.append(gates.AndGate([self.internalWiring[0]],[self.internalWiring[1]]))
        self.components.append(gates.AndGate([self.internalWiring[0]],x1, [o[1]]))
        self.components.append(gates.AndGate(x0, [self.internalWiring[1]], [o[2]]))
        self.components.append(gates.AndGate(x0,x1,[o[3]]))
