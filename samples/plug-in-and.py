from pyarch.utils import ioManager
from pyarch.connectors import transport
from pyarch.combinational import gates

inputA = transport.wires(1)
inputB = transport.wires(1)
inputC = transport.wires(1)

hWare = gates.AndGate(inputA, inputB, inputC)
ioHandler = ioManager.StringIO(hWare)

print(ioHandler.input('1','1'))
