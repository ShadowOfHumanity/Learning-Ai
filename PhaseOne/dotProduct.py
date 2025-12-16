x = [1, 2, 3]
w = [0.1, 0.2, 0.3]

def dotProduct (a, b):
    assert len(a) == len(b)
    return sum(a[i] * b[i] for i in range(len(a)))

        
