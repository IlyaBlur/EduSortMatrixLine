import  time as t
import LineGen as LG
import MatrixGen as MG

start = t.time()

L = [] #list(map(int,input("Введите масcив: ").split()))

def what_to_gen(L):
    choice = input("Что бы вы хотели сгенерировать М-матрица, L - строка: ")
    if choice == "L" or "l" or "д" or "Д":
        L = LG.LineGenerator()
    elif choice == "M" or "m" or "ь" or "Ь" or "М":
        L = MG.matrixP()
    else:
        print("Ошибка при выборе: ")
    return L

what_to_gen(L)




def bubble_sort (L):
    for i in range(len(L)-1):
        for j in  range(len(L)-1):
            if L[j]>L[j+1]:
                L[j], L[j+1] = L[j+1],L[j]
    print(L)
    return
# bubble_sort(L)

def Flag_Bubble_sort (L):
    for j in range(len(L)-1):
        flag = True
        for i in range(len(L)-1-j):
            if L[i]>L[i+1]:
                flag=False
                L[i],L[i+1] = L[i+1], L[i]
        if flag == True:
            break
    print(L)
    return
# Flag_Bubble_sort(L)

def selection_sort_min (L):
    for i in range (len(L)):
        min_index = i
        for j in range(i+1,len(L)):
            if L[j]<L[min_index]:
                min_index=j
        L[i],L[min_index]=L[min_index], L[i]
    return L
# print(selection_sort(L))

def selection_sort_max (L):
    for i in range(len(L)):
        imax=0
        for j in range(1, len(L)-i):
            if L[j]>L[imax]:
                imax=j
        L[imax],L[len(L)-i-1] = L[len(L)-i-1],L[imax]
    return L

print(selection_sort_max(L))

finish = t.time()
res_msec = (finish-start)*1000

print(res_msec)


