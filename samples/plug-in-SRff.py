import sys
sys.path.insert(0, '../utils')
import ioManager
import new
sys.path.insert(0, '../connectors')
import transport
sys.path.insert(0,'../sequential')
import ff

inputS = transport.wires(1)
inputR = transport.wires(1)
out = transport.wires(2)
clock = transport.wires(1)
hware = ff.SRFlipFlop(inputS,inputR,out,clock)
iohandler = ioManager.StringIO(hware)

print iohandler.input('0','1','1')
