N = 0
M = 0
matrix = []
def matrixP ():
    global matrix,N,M
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))
    for i in range(N):
        value = (list(map(int, input(f"Введите {M} чисел для {i+1} строки через пробел: ").split())))
        if len(value) > M:
            print("Превышено допустимое количество элементов: ")
            break
        else:
            matrix.append(value)
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
    return matrix


def MatrixGen1Line(N,matrix):
    print("Печать матрицы с 1 главной диагональю: ")
    for j in range(N):
        value = [(1 if j==i else 0)for i in range(N)]
        matrix.append(value)
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

# MatrixGen1Line(N, matrix)

def MatrixGen2Lines(N,matrix):
    print("Печать матрицы с двумя диагоналями: ")
    for j in range(N):
        value = [(1 if j==i or i+j==N-1 else 0)for i in range(N)]
        matrix.append(value)
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
    return

# MatrixGen2Lines(N, matrix)