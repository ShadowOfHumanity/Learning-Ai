import dotProduct

def matrixVectorMul(matrix, vector):
    results = []
    for row in matrix: # if im right, a row is a vector
        results.append(dotProduct.dotProduct(row, vector))
    return results


myMatrix = [
            [1, 2, 3],
            [4, 5, 6]
           ]

myVector = [7, 8, 9]

print(matrixVectorMul(myMatrix, myVector))