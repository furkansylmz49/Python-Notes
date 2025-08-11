from time import time

def logger(func):
    def wrapper(*args,**kwargs):
        print(f"[LOG] {func.__name__} başladı...")
        result = func(*args,**kwargs)
        print(f"[LOG] {func.__name__} bitti.")
        return result
    return wrapper



def check_data(func):
    def wrapper(data,*args,**kwargs):
        if not(data):
            print("Hata: Veri boş!")
            return
        else:
            return func(data,*args,**kwargs)
    return wrapper


def timer(func):
    def wrapper(*args,**kwargs):
        start = time()
        result = func(*args,**kwargs)
        end = time()
        print(f"{func.__name__} süresi: {end - start:.6f} saniye")
        return result
    return wrapper



@logger
@check_data
@timer
def process_data(data):
    squares = [x**2 for x in data]
    print("Kareler:", squares)
    return squares

process_data([1, 2, 3, 4])
print()
process_data([])