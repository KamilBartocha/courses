def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start!")
        return func(*args, **kwargs)
    return wrapper

@greeting_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))



def type_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f"Typ argumentu: {type(arg).__name__}")
        return func(*args, **kwargs)
    return wrapper

@type_decorator
def echo(value):
    return value

print(echo("Hello"))  # Powinno wypisać "Typ argumentu: str" i "Hello"
print(echo(10))      # Powinno wypisać "Typ argumentu: int" i "10"




import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania: {end_time - start_time:.4f} sekund")
        return result
    return wrapper

@time_decorator
def long_running_function(n):
    time.sleep(n)
    return "Gotowe!"

print(long_running_function(2))  # Czas wykonania będzie wynosić około 2 sekund
