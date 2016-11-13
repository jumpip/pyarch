import sys
sys.path.insert(0, '../utils')
import ioManager
import new
sys.path.insert(0, '../connectors')
import transport
sys.path.insert(0,'../combinational')
import arithmetics

inputA = transport.wires(4)
inputB = transport.wires(4)
out = transport.wires(5)
hware = arithmetics.PipoAdder(inputA,inputB,out)
iohandler = ioManager.StringIO(hware)

print iohandler.input('1111','1111')
