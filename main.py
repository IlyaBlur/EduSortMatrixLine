import LineGen as LG
from MatrixGen import Matrix
import time




# L = 0 #list(map(int,input("Введите масcив: ").split()))
#
# def what_to_gen():
#     global L
#     choice = input("Что бы вы хотели сгенерировать М-матрица, L - строка: ")
#     if choice in ["L","l", "д","Д"]:
#         L = LG.LineGenerator()
#     elif choice in ["M" ,"m" , "ь", "Ь", "М"]:
#         L = MG.MatrixGenerateRandom()
#     else:
#         print("Ошибка при выборе: ")
#     return L
#
#
# what_to_gen() #????
#
# def sort_choise(L):
#     choice = input("Как бы вы хотели остортировать")

start = 0
# L = []
# M = []
# maxElem = []
#
# try:
#     choice = input("Что бы вы хотели сгенерировать М-матрица, L - строка: ")
#     if choice in ["L","l", "д","Д"]:
#         start = time.time()
#         L = LG.LineGenerator()
#         Sorts.insertion_sort_with_pop(L)
#     elif choice in ["M","m", "ь", "Ь", "М"]:
#         start = time.time()
#         M = MG.MatrixGenerateRandom()
#         MP.MaxRowElem(maxElem,M)
# except ValueError:
#     print("Ошибка при вводе данных: ")
#
# finish = time.time()
# res_msec = (finish-start)*1000
#
# print(res_msec)


# if __name__=="__main__":

def what_to_gen():
    choice = input("Что бы вы хотели сгенерировать М - матрица, L - строка: ").lower()
    CHOICES[choice]()

def matrix():
    start = time.time()
    M = Matrix()
    if M.error:
        return
    how_to_gen = input("Введите как сгенерировать матрицу \n R - рандомная \n S - по введенным данным \n 1M - матрица с одной главной диагональю \n 2M - с двумя диоганалями: ").lower()
    if how_to_gen in ["r","к"]:
        M.MatrixGenerateRandom()
    elif how_to_gen in ["s", "ы"]:
        M.matrixP()
    elif how_to_gen in ["1m","1ь", "1м"]:
        M.MatrixGen1Line()
    elif how_to_gen in ["2m","2ь", "2м"]:
        M.MatrixGen2Lines()
    finish = time.time()
    res_msec = (finish - start) * 1000
    print(res_msec)
    return M

def line ():
    start = time.time()
    L = LG.LineGenerator()
    finish = time.time()
    res_msec = (finish - start) * 1000
    print(res_msec)
    return L

CHOICES = {"l": line,
           "д": line,
           "m": matrix,
           "ь": matrix,
           "м": matrix,
           "v": matrix,
           }

what_to_gen()
