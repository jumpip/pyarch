class StringIO:

  def __init__(self,ioMapping):
    self.i = ioMapping.input
    self.o = ioMapping.output

  def input(self,*args):
    inpIndex = len(args[0]) - 1
    totalInps = len(self.i)
    pos = 0
    while inpIndex >= 0:
      for inpNum in range(totalInps):
        self.i[inpNum][pos].propagateSignal(int(args[inpNum][inpIndex]))
      pos += 1
      inpIndex -= 1

    out = list()
    for i in self.o:
        out.append(str(i.getSignal()))
    outBuff = "".join(out)
    return outBuff
