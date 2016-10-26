import sys
sys.path.insert(0, '../utils')
import ioManager
import new
sys.path.insert(0, '../connectors')
import transport
sys.path.insert(0,'../combinational')
import arithmetics

inputA = transport.wires(3)
out = transport.wires(2)
hware = arithmetics.FullAdder(inputA,out)
iohandler = ioManager.StringIO(hware)

print iohandler.input('011')s
