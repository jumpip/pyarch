import sys
sys.path.insert(0, '../utils')
import ioManager
import new
sys.path.insert(0, '../connectors')
import transport
sys.path.insert(0,'../combinational')
import gates
from functools import partial
class GrayCode_CVT(new.Hardware,object):
    def __init__(self,inp,out):
        super(GrayCode_CVT,self).__init__([inp,out])
        input=[]
        input.append(inp)
        self.input=input
        self.output=out
        inp[0].on('signal',partial(self.hardware,inp,out))
        self.components.append(gates.XorGate([inp[0]],[inp[1]],[out[1]]))
        self.components.append(gates.XorGate([inp[1]],[inp[2]],[out[2]]))
        self.components.append(gates.XorGate([inp[2]],[inp[3]],[out[3]]))

    def hardware(self,inp,out):
        sig = inp[0].getSignal()
        if sig:
            out[0].propagateSignal(1)
        else:
            out[0].propagateSignal(0)


inputA = transport.wires(4)
out = transport.wires(4)
hware = GrayCode_CVT(inputA,out)
iohandler = ioManager.StringIO(hware)

print iohandler.input('1001')
