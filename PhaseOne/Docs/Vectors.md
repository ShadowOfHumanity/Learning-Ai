# **Vectors (The Atom of ML)**


### **What a Vector is**
A vector is just: <br />
``[x1, x2, x3, ..., xn]`` <br />
In ML:
- Inputs are vectors
- Weights are vectors
- Outputs are vectors

----
### **Dot Product (Critical)**
``x . w = x1*w1 + x2*w2 + ... + xn*wn`` where x, w are vectors <br/>

This is:
> How models "combine" features

----

### **Code Task**
Write dot product **Without NumPy**
<br />
[code here](../dotProduct.py)

----
### **Why This Matters**
Every neuron does:
``output = dot(inputs, weights) + bias``<br/>
You've just built a 'neuron core'