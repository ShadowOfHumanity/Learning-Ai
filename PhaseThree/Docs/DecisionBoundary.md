## **Decision Boundary (The Big Insight)**

### **Concept**
The model predicts class 1 if:
``y_hat >= 0.5`` <br/>

That means:
``w . x + b >= 0`` <br/>

Logistic regression is a linear seperator

----
### **Visualization insight**
- In 2D -> Line
- in 3D -> Plane
- in N-D -> Hyperplane

----
### **Final Tasks (Important)**
1. Write down what each variable means without looking
    - w = weight, b = bias, x = input/feature, y = truthful result, y_hat = prediction (after sigmoid or if only linear regression), z = linear regression prediction, lr = learning rate, jumps in learning depends how big this is.

2. Explain why sigmoid is needed
    - Gives a "decisive" response and confidence in the prediction. (range {0-1})

3. Explain what ``y_hat - y`` represents
    - This function represents the Error (difference between truth and prediction)

4. Expalin why logistic regression is a neural network with **one neuron**
    - Logistic regression is a neural network with one neuron because it performs the exact same operations: it takes inputs, computes a weighted sum (w·x + b), and applies an activation function (sigmoid). A neuron is just this basic computation unit, and logistic regression has exactly one of them.

