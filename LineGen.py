import time as t
import random


def LineGenerator ():
    count = int(input("Введите колличество чисел для генерации: "))
    #start=t.time()
    F = []
    for i in range(count):
        F.append(random.randint(-1000000,1000000))
    print(F)
    #print("Working time: ", t.time()-start)
    return F



#print(LineGenerator())