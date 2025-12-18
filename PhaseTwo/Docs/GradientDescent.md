## **Gradient Descent**

### **Concept*
We update parameters **against the gradient**

```
w = w − α · ∂L/∂w
b = b − α · ∂L/∂b
```
- ``α`` = learning rate
- Controls speed vs stability

**Intuition:**

- Large α → jumpy
- Small α → slow

```py
def train_step(x, y, w, b, lr):
    y_hat = predict(x, w, b) # linear regression
    error = y_hat - y # lin. regression pred. value - real value

    for i in range(len(w)):
        w[i] -= lr * 2 * error * x[i]
        # this is gradient descent

    b -= lr * 2 * error # updating bias term in gradient descent
    return w, b
```
notes:
- w[i] = the i-th weight
- lr = learning rate
- error = y_hat - y
- x[i] = the i-th input feature