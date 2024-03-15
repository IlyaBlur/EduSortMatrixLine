from MatrixGen import matrix,N

Average = []
def MinusToAverege(matrix,Average,N):
    print("Замена отрицательных элементов на среднее значение положительных в строке: ")
    for j in range(N):
        positive_numbers = [x for x in matrix[j] if x>0]
        average =round(sum(positive_numbers)/len(positive_numbers), 2) if positive_numbers else 0
        modified_row = [x if x > 0 else average for x in matrix[j]]
        Average.append(modified_row)
    for row in Average:
        for elem in row:
            print(elem, end=" ")
        print()
    return Average

MinusToAverege(matrix,Average,N)




MaxElem = []
def MaxRowElem (MaxElem,matrix):
    print("Максимальные значение по строкам: ")
    for row in matrix:
        value = [int(max(row))]
        MaxElem.append (value)
    for row in MaxElem:
        for elem in row:
            print(elem, end= " ")
        print()
    return

# MaxRowElem(MaxElem,matrix)

def MaxСolumnElem (MaxElem,matrix,M):
    print("Максимальные значение по столбцам: ")
    value = [max(row[i] for row in matrix) for i in range(M)]
    MaxElem.append(value)
    for row in MaxElem:
        for elem in row:
            print(elem)
        print()
    return

# MaxСolumnElem(MaxElem,matrix,M)