## **The Model**

We are answering **ONE** question:

> **How can a machine discover a relationship between numbers by itself?**
----

### **1. What Problem Are We Solving?**
We have data:
`x -> y`
Examples:
```
house size -> price
hours studied -> grade
features -> outcome
```
We assume:
> y depends approximately linearly on x

So we choose a model family:
``y ≈ w·x + b`` or ``y ≈ w*b + b``

### Linear Regression (1 Feature)
Note: there is a 1 feature adn multi feature linear regression, the multi feature was previously talked on [here](../PhaseOne/predict.py)

Model:
```
y = w * x + b
```
- ``w`` -> weight (slope)
- ``b`` -> bias (offset)
This predicts a number

----

## **Some special notes**

### The result of linear regression, is often called y_hat or ŷ
