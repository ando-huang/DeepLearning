def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def convolute(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    output = [[0 for col in range(cols-1)] for row in range(rows-1)]
    convolute = [[2, 0], [0, 1]]
    for i in range(len(output)):
        for j in range(len(output[0])):
            output[i][j] = matrix[i][j] * 1 + matrix[i+1][j+1] * 2 
    return output

def inputMatrix():
    rows = int(input())
    cols = int(input())
    matrix = []
    for i in range(rows):
        row = list(input().strip().split())
        matrix.append(row)
    return matrix

testMatrix = [
    [0, 10, 10, 0],
    [20, 30, 30, 20],
    [10, 20, 20, 10],
    [0, 5, 5, 0]
]
printMatrix(convolute(testMatrix))