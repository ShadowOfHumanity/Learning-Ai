import dotProduct as dp

def predict(x, w, b):
    # linear regression prediction
    return dp.dotProduct(x, w) + b

test_x = [1, 2, 3]
test_w = [0.2, 0.4, 0.6]

test_b = 0.5
print(predict(test_x, test_w, test_b))