
def flippingMatrix(matrix):
    # Write your code here
    rows = len(matrix)
    cols = len(matrix[0])
    sum = 0
    for i in range(0, rows//2):
        for j in range(0, cols//2):
            sum += max(matrix[i][j], matrix[i][cols-j-1], matrix[rows-1-i][j], matrix[rows-1-i][cols-1-j])

    return sum



q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())

    matrix = []

    for _ in range(2 * n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = flippingMatrix(matrix)

    fptr.write(str(result) + '\n')

fptr.close()
