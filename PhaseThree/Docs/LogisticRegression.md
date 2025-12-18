## **Logistic Regression (Classification)

### **Regression vs Classification (What changed?)**
**Regression**

output:
``ŷ ∈ ℝ``
Examples:
- price
- Temperature
- Score
----

**Classification**
``ŷ ∈ {0, 1}``
Examples:
- Spam / Not Spam
- Fraud / Not Fraud
- Win / Lose

We are not predicting a number, we're predicting a decision.

----
### **Key Problem**

Linear Regression Outputs
``ŷ = w·x + b``
<br/>But this can be: ``−100, 2.3, 5000
`` <br />
That doesnt look like a probability.

----
**Task**
> Why is linear regression bad for yes/no decisions?
```
It doesnt output a yes or no (0 to 1), 
it can output 1.8 => 180% ?? 
or -0.5 => Negative probability doesnt exist??
```