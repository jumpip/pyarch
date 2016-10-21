class StringIO:

  def __init__(ioMapping):
    inputGroup = len(ioMapping) - 1
    self.i = ioMapping[0:inputGroup]
    self.o = ioMapping[inputGroup]

  def input(*args):
    inpIndex = len(args[0]) - 1
    totalInps = len(self.i)
    pos = 0
    while inpIndex >= 0:
      for inpNum in range(totalInps):
        self.i[inpNum][pos].propagateSignal(int(args[inpNum][inpIndex]))
      pos += 1
      inpIndex -= 1

    outBuff = map(wire.getSignal(), self.o)
    outBuff = "".join(outBuff)
    return outBuff

