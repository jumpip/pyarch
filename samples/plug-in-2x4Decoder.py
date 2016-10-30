from pyarch.utils import ioManager
from pyarch.connectors import transport
from pyarch.combinational import decoders

inputA = transport.wires(1)
inputB = transport.wires(1)
output = transport.wires(4)

iohandler = ioManager.StringIO(decoders.Decoder2x4(inputA,inputB,output))

print iohandler.input('0','1')
