
def mse(y_pred, y_true):
    return (y_pred - y_true) **2

# test with fake values
#test_y_pred = 3.5
#test_y_true = 4.0
#print(mse(test_y_pred, test_y_true))