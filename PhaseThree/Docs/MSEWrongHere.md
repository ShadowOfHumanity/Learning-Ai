## **Why MSE is WRONG here**

### **Problem**
If we use:
``Loss = (ŷ − y)²`` <br/>
(Loss = prediction - y)² <br/>
Bad things happen:
- Slow learning
- Vanishing gradients
- Poor probability interpretation

----
### **Correct Loss: Log Loss (Cross-Entropy)**
``Loss = − [ y·log(ŷ) + (1−y)·log(1−ŷ) ]`` <br />
Loss = -[ y . log(prediction) + (1-y) . log(1 - prediction)]

----
### **Why This Loss?
- Penalizes confident wrong predictions HARD
- Comes from probability theory
- Works with sigmoid perfectly

----
### **Task**
Think:
> Why is it worse to predict 0.01 than 0.4 when the true value is 1?

Because 0.01 is not only far from 1, but the model was also very confident in its wrong prediction.