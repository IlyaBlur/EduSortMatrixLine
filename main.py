from LineGen import LineGenerators as LG
from MatrixGen import Matrix
import Sorts
import matrix_processing as MP
import time


def what_to_gen():
    choice = input("Что бы вы хотели сгенерировать М - матрица, L - строка: ").lower()
    result = CHOICES[choice]()
    return choice, result


def matrix():
    start = time.time()
    M = Matrix()
    if M.error:
        return
    how_to_gen = input(
        "Введите как сгенерировать матрицу \n R - рандомная \n S - по введенным данным \n 1M - матрица с одной главной диагональю \n 2M - с двумя диоганалями: ").lower()
    if how_to_gen in ["r", "к"]:
        M.MatrixGenerateRandom()
    elif how_to_gen in ["s", "ы"]:
        M.matrixP()
    elif how_to_gen in ["1m", "1ь", "1м"]:
        M.MatrixGen1Line()
    elif how_to_gen in ["2m", "2ь", "2м"]:
        M.MatrixGen2Lines()
    else:
        print("Неверный выбор")
    finish = time.time()
    res_msec = (finish - start) * 1000
    print(res_msec)
    return M


def line():
    l = LG()
    how_to_gen = input("Введите как сгенерировать строку\n R - рандомная\n S - по введенным данным: ")
    if how_to_gen in ["r", "к"]:
        l.LineGeneratorRandom()
    elif how_to_gen in ["s", "ы"]:
        l.LineGenInput()
    else:
        print("Неверный выбор")
    return l.L


CHOICES = {"l": line,
           "д": line,
           "m": matrix,
           "ь": matrix,
           "м": matrix,
           "v": matrix,
           }

c, r = what_to_gen()
if c in ["l", "д"]:
    sort_type = input("Введите как сортировать\n b - сортировка пузырьком\n fb - Сортировка пузырьком с флагом\n "
                      "smin - сортировка выбором min\n smax - сортировка выбором max\n is - сортировка вставками\n isp - сортировка вставками pop: ").lower()
    print(r)
    if sort_type in ["и", "b"]:
        Sorts.bubble_sort(r)
    elif sort_type in ["fb", "аи"]:
        Sorts.Flag_Bubble_sort(r)
    elif sort_type in ["sm", "ыи"]:
        Sorts.Flag_Bubble_sort(r)
    elif sort_type in ["smax", "ыьфч"]:
        Sorts.selection_sort_max(r)
    elif sort_type in ["smin", "ыьшт"]:
        Sorts.selection_sort_min(r)
    elif sort_type in ["is", "шы"]:
        Sorts.insertion_sort(r)
    elif sort_type in ["isp", "шыз"]:
        Sorts.insertion_sort_with_pop(r)
    else:
        print("Ошибка при выборе")
elif ["m", "ь", "м", "v"]:
    sort_type = input(
        "Что сделать с матрицей?\n mta - заменить отрицательные элементы на суммы положительных в строке\n mre - вывести максимальное значение по строкам \n"
        "mce - Вывести максимальные значения по столбцам: ")
    print(r.matrix)
    if sort_type in ["mta", "ьеф"]:
        MP.MinusToAverege(r)
    elif sort_type in ["mre", "ьку"]:
        MP.MaxRowElem(r)
    elif sort_type in ["mce", "ьсу"]:
        MP.MaxСolumnEelem(r)
    else:
        print("Ошибка при выборе")
