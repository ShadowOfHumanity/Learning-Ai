## **Training Loop (Concept First)**

### **One Training Step**

1. [Compute ``z = w . x + b``](./LogisticRegression.md)
2. [Apply sigmoid -> ``y_hat``](./LogisticRegressionModelExp.md)
3. [Compute loss (Log Loss)](./MSEWrongHere.md)
4. [Compute Gradients](./Gradients.md)
5. [Update Parameters](../../PhaseOne/Docs/Foundations.md)
Same loop as linear regression

----
Minimal code:
```python
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))
```
```python
def predict_prob(x,w,b):
    z = sum(x[i] * w[i] for i in range(len(w))) + b
    return sigmoid(z)
```
```python
def train_step(x, y, w, b, lr):
    y_hat = predict_prob(x, w, b)
    error = y_hat - y

    for i in range(len(w)):
        w[i] -= lr * error * x[i]

    b -= lr * error
    return w, b
```

