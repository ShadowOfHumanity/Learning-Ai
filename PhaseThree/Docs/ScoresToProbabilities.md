## **From Scores to Probabilities**

### *Idea*
We still want:

``score = w.x + b``
but now we interpret it as:
> "How confident am i?"

We need to squash it into (0, 1)

----

### **Sigmoid Function**
```
σ(z) = 1 / (1 + e^(−z))
```
Where:
- ``z = w.x + b``
- Output ≈ probability
----

| z             | σ(z) |
| ------------- | ---- |
| very negative | ~0   |
| 0             | 0.5  |
| very positive | ~1   |

----

###**Task**

1. What happens if w·x + b = 0?
    - that the prediction is 50% via sogmoid function

- Why is that useful?
    - This defines the decision, 50% is exactly on the boundry line, had it been a percentage point higher, its a "yes", if lower, then "no"