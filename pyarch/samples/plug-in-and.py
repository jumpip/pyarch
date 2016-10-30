import sys
sys.path.insert(0, '../utils')
import ioManager
import new
sys.path.insert(0, '../connectors')
import transport
sys.path.insert(0,'../combinational')
import gates

inputA = transport.wires(1)
inputB = transport.wires(1)
inputC = transport.wires(1)

hWare = gates.AndGate(inputA, inputB, inputC)
ioHandler = ioManager.StringIO(hWare)

print(ioHandler.input('1','1'))
