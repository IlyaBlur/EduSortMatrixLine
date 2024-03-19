import numpy as np

class Matrix:
    def __init__(self):
        self.matrix = []
        self.error = False
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
        # self.matrix_print()
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