## **Why We Need Gradients**

We want to adjust ``w`` and ``b`` so loss goes down

To do that, we need:

```
∂loss / ∂w
∂loss / ∂b
```
**The derivative of loss with respect to w**
e.g:
```
loss = 20w³ +  3b² + 2wb
then
∂loss / ∂w = 60w² + 2b (we treat b as a constant)
∂loss / ∂b = 6b + 2w (we treat w as a constant)
```
----
### **Loss:**
` L = (wx + b - y)²`
### **Derivatives:**
```
∂L/∂w = 2(wx + b - y) * x 
∂L/∂b = 2(wx + b - y)
```

This is the **entire secret** of training.

### **Gradients, give the direction of steepest increase or steepest dicrease, the steeper the better**