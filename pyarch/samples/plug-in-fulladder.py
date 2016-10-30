from pyarch.utils import ioManager
from pyarch.connectors import transport
from pyarch.combinational import arithmetics

inputA = transport.wires(3)
out = transport.wires(2)
hware = arithmetics.FullAdder(inputA,out)
iohandler = ioManager.StringIO(hware)

print iohandler.input('011')  # 'carry bit + 2 sum bits'
