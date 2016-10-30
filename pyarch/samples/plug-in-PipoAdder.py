from pyarch.utils import ioManager
from pyarch.connectors import transport
from pyarch.combinational import arithmetics

inputA = transport.wires(4)
inputB = transport.wires(4)
out = transport.wires(5)
hware = arithmetics.PipoAdder(inputA,inputB,out)
iohandler = ioManager.StringIO(hware)

print iohandler.input('1111','1111')
