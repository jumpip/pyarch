from pyarch.utils import ioManager
from pyarch.connectors import transport
from pyarch.sequential import ff

inputS = transport.wires(1)
inputR = transport.wires(1)
out = transport.wires(2)
clock = transport.wires(1)
hware = ff.SRFlipFlop(inputS,inputR,out,clock)
iohandler = ioManager.StringIO(hware)

print iohandler.input('0','1','1')  # S-bit R-bit Clock
