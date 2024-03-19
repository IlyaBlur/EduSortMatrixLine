from MatrixGen import Matrix


def MinusToAverege(matrix: Matrix):
    print("Замена отрицательных элементов на среднее значение положительных в строке: ")
    average = []
    for j in range(matrix.N):
        positive_numbers = [x for x in matrix.matrix[j] if x > 0]
        av = round(sum(positive_numbers) / len(positive_numbers), 2) if positive_numbers else 0
        modified_row = [x if x > 0 else av for x in matrix.matrix[j]]
        average.append(modified_row)
    for row in average:
        for elem in row:
            print(elem, end=" ")
        print()
    return average


def MaxRowElem(matrix: Matrix):
    max_elem = []
    print("Максимальные значение по строкам: ")
    for row in matrix.matrix:
        value = [int(max(row))]
        max_elem.append(value)
    for row in max_elem:
        for elem in row:
            print(elem, end=" ")
        print()
    return max_elem


def MaxСolumnEelem(matrix: Matrix):
    print("Максимальные значение по столбцам: ")
    max_elem = []
    value = [max(row[i] for row in matrix.matrix) for i in range(matrix.M)]
    max_elem.append(value)
    for row in max_elem:
        for elem in row:
            print(elem)
        print()
    return

# MaxСolumnElem(max_elem,matrix,M)
