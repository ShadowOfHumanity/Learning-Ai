from LinnearRegression1D import predict

# 1. The Setup
# We have a sequence that looks like it follows a pattern:
# Input (x): 1, 2, 3, 4
# Output (y): 2, 4, 6, 8
#
# Our brain sees the pattern "times 2".
# "Times 2" in math is: y = 2 * x + 0
# So: weight (w) = 2, bias (b) = 0

w = 2
b = 0
x_to_predict = 5

# 2. The Prediction
# We use the model (the equation) to predict the next value.
prediction = predict(w, x_to_predict, b)

print("--------------------------------------------------")
print(f"Pattern found: y = {w}x + {b}")
print(f"Predicting for input: {x_to_predict}")
print(f"Model calculation: {w} * {x_to_predict} + {b}")
print(f"Prediction result: {prediction}")
print("--------------------------------------------------")
