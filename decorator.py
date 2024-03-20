import time as t

def timing_decorator(func):
    def wrapper():
        start = t.time()
        func()
        finish = t.time()
        print(f"Функции {func.__name__} выполнялась {finish - start:.2f} секунд")
    return wrapper()