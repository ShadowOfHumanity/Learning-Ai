## **Gradients (What Actually Updates)**

### **Loss depends on:**
```
w, b → z → ŷ → Loss
```
(weight, bias, prediction, sigmoided prediction, loss )
Chain reaction.

----

### **Resulting Gradients (Given)**
```
∂L/∂w = (ŷ − y) x
∂L/∂b = (ŷ − y)
```

This shows that its cleaner, as there are no more factors of 2

----

### **Meaning**
- ``(ŷ − y)`` = prediction error
- `x` = feature influence

----

### **Task**
Explain:
> Why does a feature with value 0 not affect learning

This is because the weights will result to nothing, because ``0 x w[i] = 0``