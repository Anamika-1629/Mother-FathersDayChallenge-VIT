def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

if __name__ == "__main__":
    import ast
    matrix = ast.literal_eval(input("Enter 2D matrix (e.g. [[1,2,3],[4,5,6],[7,8,9]]): "))
    rotate(matrix)
    print(matrix)
