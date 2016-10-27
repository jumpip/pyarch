import sys
sys.path.insert(0, '../utils')
import ioManager
import new
sys.path.insert(0, '../connectors')
import transport
sys.path.insert(0,'../combinational')
import decoders

inputA = transport.wires(1)
inputB = transport.wires(1)
output = transport.wires(4)

iohandler = ioManager.StringIO(decoders.Decoder2x4(inputA,inputB,output))

print iohandler.input('0','1')
