import gates
import sys
sys.path.insert(0, '../utils')
import new
sys.path.insert(0, '../connectors')
import transport

class HalfAdder(new.Hardware):
     def __init__(self,x,s):
                try:
                        (len(x) != 2 or len(s) != 2)
                except NotImplementedError:
                        print('Invalid Connections')
                super(HalfAdder,self).__init__([x, s])
                self.components.append(gates.XorGate([x[0]],[x[1]],[s[1]]))
                self.components.append(gates.AndGate([x[0]],[x[1]],[s[0]]))

class FullAdder(new.Hardware):
    def __init__(self,x,s):
        try:
            (len(x0)!=3 or len(s)!=2)
        except NotImplementedError:
            print('Invalid Connections')
        super(FullAdder,self).__init__([x,s])
        self.internalWiring = wires(3)
        self.components.append(HalfAdder([x[0],x[1]], self.internalWiring[0], self.internalWiring[1]))
        self.components.append(HalfAdder([self.internalWiring[1],x[2]],[self.internalWiring[2],s[1]]))
        self.components.append(gates.OrGate([self.internalWiring[0]],[self.internalWiring[2]],[s[0]]))
        
                            
