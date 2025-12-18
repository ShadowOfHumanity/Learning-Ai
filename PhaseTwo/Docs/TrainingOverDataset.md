## **Training Over a Dataset**

### **Concept**
One data point != learning

We repeat:
- Over all samples
- Multiple time (epochs)

```py

for epoch in range(epochs):
    for x, y in data:
        w, b = train_step(x, y, w, b, lr)
        # weight, bias = ...
```
Each epoch:
- Reduces loss
- Improves predictions

----
### **Insight**

Training = repeated small corrections.

> Neural networks are nothing more than stacked linear regressions with non-linearities