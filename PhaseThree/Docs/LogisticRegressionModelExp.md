## **The Logistic Regression Model (Variables Explained)

### **Full Model**
``ŷ = σ(w·x + b)`` <br/>

### **Variables (Very Imp)**
- `x` -> input feature vector
Example: `[hours_studied, sleep_hours]`
- `w` -> weight vector
importance of each feature
- `b` -> bias
Baseline tendency
- `z` -> raw score (`w.x + b`)
- `σ(z)` → probability of class 1
- `ŷ` → predicted probability
- `y` → true label (`0` or `1`)

----
### **Interpretation**
if: ``ŷ = 0.87``
Model says:
> 87% confident this is class 1 (yes, positive)

----
### **Task**
Explain in words:
> What does a large positive weight mean:
A large weight means that the feature strongly influences the prediction towards class 1