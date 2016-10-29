# PyArch
#### Hardware Abstraction Library in Python 


1. [About PyArch](#about-pyarch)
2. [Why PyArch](#why-pyarch)
3. [Capabilities](#capabilities)
4. [Installation](#installation)
5. [Inbuilt Abstractions](#inbuilt-abstractions)
6. [How To Use?](#how-to-use)
7. [Create your own custom abstraction](#creating-a-custom-hardware-abstraction)
8. [Contributors](#contributors)

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
  - NandGate
  - OrGate
  - NorGate
  - XorGate      
  - NotGate
- Decoders
  - Decoder 1x2
  - Decoder 2x4
- Arithmetic circuits
  - Half Adder
  - Full Adder
  - Parallel-in Parallel-out Adder
- Asynchronous timing circuits
  - S-R flip flop
  - D flip flop

### How to use?
See [Samples](samples/)

### Creating a custom Hardware Abstraction

**Some Basic Rules**
- Every Class/hardware extends on Hardware.
- Every Class must be declared as [New-Style](https://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes) not Classic-Style. 
- All the logic goes inside the hardware method of your component's Class.
- With the help of getSignal and propagateSignal methods of Wire, read changes from input Wire instances, use your logic on them, and emit result through the output Wire instance.

Example:  
```python
        class NotGate(new.Hardware,object):
                def __init__(self,x,o):
                        try:
                                (len(x) != 1 or len(o) != 1)
                        except NotImplementedError:
                                print('Invalid Connections')
                        super(NotGate,self).__init__([x, o])
                        input = []      
                        input.append(x)      
                        self.input = input  # A list of all the inputs   
                        self.output = o   
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
```
###Create using already existing Abstractions
Let's create a Binary to Gray code convertor  

Example:
```python
class GrayCode_CVT(new.Hardware,object):
    def __init__(self,inp,out):
        super(GrayCode_CVT,self).__init__([inp,out])
        input=[]
        input.append(inp)   
        self.input=input
        self.output=out
        inp[0].on('signal',partial(self.hardware,inp,out))   #MSB remains same after conversion
        self.components.append(gates.XorGate([inp[0]],[inp[1]],[out[1]]))  
        self.components.append(gates.XorGate([inp[1]],[inp[2]],[out[2]]))
        self.components.append(gates.XorGate([inp[2]],[inp[3]],[out[3]]))

    def hardware(self,inp,out):
        sig = inp[0].getSignal()
        if sig:
            out[0].propagateSignal(1)
        else:
            out[0].propagateSignal(0)
```
##### Inspired from [Architect](https://github.com/mbad0la/Architect)

### Contributors
<!-- Contributors START
Prachi Manchanda prachi1210 https://github.com/prachi1210 code doc
Jeevesh Narang JeeveshN https://github.com/JeeveshN code doc
Mansimar Kaur mansimarkaur https://github.com/mansimarkaur doc
Contributors END -->
<!-- Contributors table START -->
| [![Jeevesh Narang](https://avatars.githubusercontent.com/JeeveshN?s=100)<br /><sub>Jeevesh Narang</sub>](https://github.com/JeeveshN)<br /> [📖]() | [![Prachi Manchanda](https://avatars.githubusercontent.com/prachi1210?s=100)<br /><sub>Prachi Manchanda</sub>](https://github.com/prachi1210)<br />[📖]() | [![Mansimar Kaur](https://avatars.githubusercontent.com/mansimarkaur?s=100)<br /><sub>Mansimar Kaur</sub>](https://github.com/mansimarkaur)<br /> [📖]() |
| :---: | :---: | :---: | 
<!-- Contributors table END -->

