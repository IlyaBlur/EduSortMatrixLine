import numpy as np

# N = 0
# M = 0
# matrix = []


# def MatrixGenerateRandom ():
#     global matrix,N,M
#     N = int(input("Введите количество строк N: "))
#     M = int(input("Введите количество столбцов M: "))
#     matrix = np.random.randint(-1000, 1000, (N,M))
#     print(matrix)
#     return matrix
#
# def matrixP ():
#     global matrix,N,M
#     N = int(input("Введите количество строк N: "))
#     M = int(input("Введите количество столбцов M: "))
#     for i in range(N):
#         value = (list(map(int, input(f"Введите {M} чисел для {i+1} строки через пробел: ").split())))
#         if len(value) > M:
#             print("Превышено допустимое количество элементов: ")
#             break
#         else:
#             matrix.append(value)
#     for row in matrix:
#         for elem in row:
#             print(elem, end=" ")
#         print()
#     return matrix
#
#
# def MatrixGen1Line(N,matrix):
#     print("Печать матрицы с 1 главной диагональю: ")
#     for j in range(N):
#         value = [(1 if j==i else 0)for i in range(N)]
#         matrix.append(value)
#     for row in matrix:
#         for elem in row:
#             print(elem, end=" ")
#         print()
#
# # MatrixGen1Line(N, matrix)
#
# def MatrixGen2Lines():
#     # global matrix, N
#     # N = int(input("Введите количество строк N: "))
#     print("Печать матрицы с двумя диагоналями: ")
#     for j in range(N):
#         value = [(1 if j==i or i+j==N-1 else 0)for i in range(N)]
#         matrix.append(value)
#     for row in matrix:
#         for elem in row:
#             print(elem, end=" ")
#         print()
#     return

# MatrixGen2Lines()

class Matrix:
    def __init__(self):
        self.matrix = []
        try:
            self.N = int(input("Введите количество строк N: "))
            self.M = int(input("Введите количество строк M: "))
        except ValueError:
            print("Ошибка при вводе данных")
            self.N = 0
            self.M = 0
            self.error = True

    def matrix_print(self):
        for row in self.matrix:
            for elem in row:
                print(elem, end=" ")
            print()
        return


    def MatrixGenerateRandom(self):
        self.matrix = np.random.randint(-1000, 1000, (self.N, self.M))
        print(self.matrix)
        return self.matrix


    def matrixP(self):
        for i in range(self.N):
            value = (list(map(int, input(f"Введите {self.M} чисел для {i + 1} строки через пробел: ").split())))
            if len(value) > self.M:
                print("Превышено допустимое количество элементов: ")
                break
            else:
                self.matrix.append(value)
        self.matrix_print()
        return self.matrix

    def MatrixGen1Line(self):
        print("Печать матрицы с 1 главной диагональю: ")
        for j in range(self.N):
            value = [(1 if j == i else 0) for i in range(self.N)]
            self.matrix.append(value)
        self.matrix_print()
        return self.matrix

    def MatrixGen2Lines(self):
        print("Печать матрицы с двумя диагоналями: ")
        for j in range(self.N):
            value = [(1 if j == i or i + j == self.N - 1 else 0) for i in range(self.N)]
            self.matrix.append(value)
        self.matrix_print()
        return self.matrix