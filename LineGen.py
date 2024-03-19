import random

class LineGenerators:
    def __init__(self):
        self.L = []
    def PrintLine(self):
        print(self.L)
    def LineGeneratorRandom (self):
        count = int(input("Введите колличество чисел для генерации: "))
        #start=t.time()
        for i in range(count):
            self.L.append(random.randint(-1000,1000))
        # self.PrintLine()
        #print("Working time: ", t.time()-start)
        return self.L

    def LineGenInput(self):
        value =list(map(int,input("Введите числа строки через пробел: ").split()))
        self.L = value
        # self.PrintLine()
        return self.L


#print(LineGenerator())