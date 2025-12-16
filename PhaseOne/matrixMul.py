
MatrixOne = [
    [1, 2, 3],
    [4, 5, 6]
]

MatrixTwo = [
    [1, 2],
    [3, 4],
    [5, 6]
]


def matrixMul(M, N):
    # before being able, we have to see if they are
    # compatible to multiply!
    # the number of columns in M, must be equal
    # to the numbers of rows in N
    if (len(M[0]) != len(N)):
        raise ValueError("Incompatible matrices")
    # Now they are equal! lets create the result matrix
    len(M) # rows of M
    len(N[0]) # columns of N 
    # result is a matrix that is len(M) x len(N[0]).. in this case: 2x2
    result = [[0 for _ in range(len(N[0]))] for _ in range(len(M))] # create the rows & columns
    # Now we have to fill in the result matrix
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(N)): # this k is for the columns of M or rows of N
                result[i][j] += M[i][k] * N[k][j]
    return result

print(matrixMul(MatrixOne, MatrixTwo))