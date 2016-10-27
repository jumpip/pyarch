# PyArch
#### Hardware Abstraction Library in Python

1. [About PyArch](#about-pyarch)
2. [Why PyArch](#why-pyarch)
3. [Capabilities](#capabilities)
4. [Installation](#installation)
5. [Inbuilt Abstractions](#inbuilt-abstractions)
6. [How To Use?](#how-to-use)
7. [Abstraction Rules](#abstraction-rules)
8. [Create your own custom abstraction](#creating-a-custom-hardware-abstraction)

### About PyArch
PyArch is basically, a hardware abstraction library that can be used to model a digital system. It provides construct for modeling the system hierarchically and supports both top-down and bottom-up design methodologies. 

### Why PyArch?
As computer science students, we were reluctant to learn a totally new language ([see VHDL](https://en.wikipedia.org/wiki/VHDL)) for hardware modelling. So, we came up with a our small-scaled version of hardware modelling in Python, a language that is pretty easy to learn!

### Capabilities
-  __Supports hierarchy__: A digital system can be modeled as a set of interconnected components; each component, in turn, can be modeled as a set of interconnected subcomponents.

        eg: A Full Adder can be implemented using two Half Adders and one Or Gate.
        
- __Supports flexible design methodologies__: 
  - **Top-down:** A top-down approach (also known as stepwise design) is essentially the breaking down of a system to gain insight into the sub-systems that make it up. In a top-down approach an overview of the system is formulated, specifying but not detailing any first-level subsystems.
  - **Bottom-up:** The bottom up design model starts with most specific and basic components. It proceeds with composing higher level of components by using basic or lower level components.
  - **Mixed:** Both, top-down and bottom-up approaches are not practical individually. Instead, a good combination of both is recommended.

- __Structural description style__: PyArch is objected oriented. Hence, it supports structural description style. Any hardware maybe emulated by specifying its sub-components using existing abstractions, or creating new ones.

- __Wide range of Abstraction levels__: Ranging from abstract behavioral descriptions [see Hardware](utils/new.py) to [precise gate level descriptions](combinational/gates.py) to hardware built on top of these abstractions ([Decoders](combinational/decoders.py), [Arithmetic circuits such as Adders](combinational/arithmetics.py))

### Installation
        We need to package it first
        
### Inbuilt Abstractions:
- Gates
  - AndGate    
  - OrGate      
  - XorGate      
  - NotGate
- Decoders
  - Decoder 1x2
  - Decoder 2x4
- Arithmetic circuits
  - Half Adder
  - Full Adder
- Asynchronous timing circuits //To do
  - S-R flip flop
  - D flip flop

### How to use?
//To do
        
        from pyarch import utils, connectors, combinational
        
        inputA = transport.wires(1)
        inputB = transport.wires(1)
        inputC = transport.wires(1)

        hWare = gates.AndGate(inputA, inputB, inputC)
        ioHandler = ioManager.StringIO(hWare)

        print(ioHandler.input('1','1'))

### Abstraction Rules
- Every Class/hardware extends on basic abstraction, Hardware.
- Every initialisation argument to the class instance has to be an array of Wire instances (obtained from the wires method).
- An array consisting of I/O wires is passed onto the parent class Hardware, with only the last element being the output parameter. It is necessary to provide every input parameter and the output parameter to be able to wrap this in a StringIO instance to do I/O operations with string arguments.
- Every class instance has two instance variables available from the parent Hardware instance :
   - **internalWiring** - Array of Wire instances (initially empty).
   - **components** - Array of abstractions used to build your hardware (initially empty).
- Your entire logic goes into your Class' constructor.
- **internalWiring** variable is used to initialise Wire instances that are not a part of the I/O for the hardware but are required to inter-connect the sub-components in your abstraction.
- **components** variable is used to store instances of subcomponents used in your hardware. This helps a designer to quickly refer to all the build blocks that went into making a particular piece of hardware.


### Creating a custom Hardware Abstraction

**Some Basic Rules**
- Every Class/hardware extends on Hardware.
- Every Class must be declared as [New-Style](https://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes) not Classic-Style. 
- All the logic goes inside the hardware method of your component's Class.
- With the help of getSignal and propagateSignal methods of Wire, read changes from input Wire instances, use your logic on them, and emit result through the output Wire instance.

Example:
        
        class NotGate(new.Hardware,object):
                def __init__(self,x,o):
                        try:
                                (len(x) != 1 or len(o) != 1)
                        except NotImplementedError:
                                print('Invalid Connections')
                        super(NotGate,self).__init__([x, o])
                        self.x = x
                        self.o = o
                        hardware = partial(hardware, self)

                def hardware(self):
                        xSig = self.x[0].getSignal()
                        try:
                                xSig
                        except NameError:
                                self.o[0].propagateSignal(undefined)
                        if(xSig == 1):
                                self.o[0].propagateSignal(0)
                        else:
                                self.o[0].propagateSignal(1)
