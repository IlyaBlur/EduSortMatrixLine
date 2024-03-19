def bubble_sort(L):
    for i in range(len(L) - 1):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    print(L)
    return


def Flag_Bubble_sort(L):
    for j in range(len(L) - 1):
        flag = True
        for i in range(len(L) - 1 - j):
            if L[i] > L[i + 1]:
                flag = False
                L[i], L[i + 1] = L[i + 1], L[i]
        if flag == True:
            break
    print(L)
    return


# Flag_Bubble_sort(L)

def selection_sort_min(L):
    for i in range(len(L)):
        min_index = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L


# print(selection_sort(L))

def selection_sort_max(L):
    for i in range(len(L)):
        imax = 0
        for j in range(1, len(L) - i):
            if L[j] > L[imax]:
                imax = j
        L[imax], L[len(L) - i - 1] = L[len(L) - i - 1], L[imax]
    return L


# print(selection_sort_max(L))

def insertion_sort(L):
    for i in range(1, len(L)):
        for j in range(i, 0, -1):
            if L[j] < L[i - 1]:
                L[i], L[i - 1] = L[i - 1], L[i]
            else:
                break
    print(L)
    return L


def insertion_sort_with_pop(L):
    for j in range(1, len(L)):
        k = j
        for i in range(j - 1, -1, -1):
            if L[j] < L[i]:
                k = i
        elem = L.pop(j)
        L.insert(k, elem)
    print(L)
    return L


