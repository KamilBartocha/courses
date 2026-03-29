# spłaszczanie listy:
# zmień listę na spłaszczoną tj pozbądź się wewnętrznych list:

# in:
# nested_list = [1, 2, [2, 4], 5, [6, 7], 10, 2]

# oczekiwany wynik:
# list = [1, 2, 2, 4, 5, 6, 7, 10, 2]


def nowe_zadanie():
    print(150 * "*")
    print("Nowe zadanie")
    print(150 * "*")

nested_list = [1, 2, [2, 4], 5, [6, 7], 10, 2]

solution_list = []

for element in nested_list:
    if type(element) == int:
        solution_list.append(element)
    elif type(element) == list:
        solution_list.extend(element)

print(solution_list)

nowe_zadanie()
#rozwiązanie 2

nested_list = [1, 2, [2, 4], 5, [6, 7], 10, 2]

solution_list = []

for element in nested_list:
    if type(element) == int:
        solution_list.append(element)
    elif type(element) == list:
        for sub_element in element:
            solution_list.append(sub_element)

print(solution_list)






# x = 5
# while x > 0:
#     print(x)

print("ala ma kota")




# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź "exit".')
# line = input('Następna linijka: ')
# while line != 'exit':
#     lines.append(line)
#     line = input('Następna linijka: ')
# print(lines)



############ 006 #################



nowe_zadanie()



def print_hello():
    print("hello")
    print("world")


print_hello()
nowe_zadanie()
print_hello()
nowe_zadanie()
print_hello()
nowe_zadanie()
print_hello()
nowe_zadanie()
print_hello()
nowe_zadanie()
print_hello()

nowe_zadanie()





def add3_3():
    result = 3 + 3
    return result

x = add3_3()
print(x)



def add4_4():
    result = 4 + 4
    return result

print(add4_4())  #print(8)

nowe_zadanie()




def add(num1, num2):
    result = num1 + num2
    return result

wynik = add(3, 4)
print(wynik)

nowe_zadanie()

def add(num1, num2, num3=0):
    result = num1 + num2 + num3
    return result

wynik = add(3, 4)
print(wynik)

wynik2 = add(3, 4, 10)
print(wynik2)


def separate_prints(section_number, char="-"):
    """
    Function for separate prints inside python file

    :param section_number: Number of section that will be displayed
    :param char: Character used for section creation, def: "-"
    """
    print(char * 60 + "  " + "Sekcja: " + str(section_number) + "  " + char * 60 + "\n")

separate_prints(1)
separate_prints(section_number=2, char="*")

separate_prints(3)






x = [3, 2, 1, 3 , 45, 1]

y = sorted(x, reverse=True)
print(y)
separate_prints(4)

from time import sleep

# def count_down(timer):
#     while timer >= 0:
#         print(f"sec: {timer}")
#         sleep(1)
#         timer = timer - 1
#     print("kaboooom")

# count_down(5)



# def count_down2(timer):
#     if timer == 0:
#         return "kaboooom"
#     else:
#         print(f"sec: {timer}")
#         sleep(1)
#         count_down2(timer=timer - 1)

# count_down2(5)










separate_prints(5)

def add(n1, n2, *args):
    result = n1 + n2
    if args:
        for el in args:
            result = result + el
    return result

print(add(2, 3))
print(add(2, 3, 4, 5))
print(add(2, 3, 4, 5, 6, 7))
print(add(2, 3, 4, 5, 6, 7, 8))
print(add(2, 3, 4, 5, 6, 7, 8, 100, 200))




def print_address(city, **kwargs):
    print(city)
    if kwargs:
        for name, value in kwargs.items():
            print(name, value)

print_address("wwa", street="Wrocławska", postal_code=31111)

separate_prints(6)


# async napisać






import time
import requests
import asyncio
import aiohttp

URL = "https://jsonplaceholder.typicode.com/todos/{}"
REQUESTS_COUNT = 100

# -------------------------------------------
# 1. THE SLOW WAY (Synchronous)
# -------------------------------------------
def run_sync():
    print("--- 1. Starting Sync (One at a time) ---")
    start = time.time()

    for i in range(1, REQUESTS_COUNT + 1):
        current_url = URL.format(i)
        response = requests.get(current_url)
        print(f"Finished request {i}, response status: {response.status_code}")

    end = time.time()
    return end - start

# -------------------------------------------
# 2. THE FAST WAY (Asynchronous)
# -------------------------------------------

async def fetch_one(session, i):
    current_url = URL.format(i)
    async with session.get(current_url) as response:
        await response.text() # wait for the result, but other tasks can run in the background
        print(f"Finished request {i}")

# This function sets up the loop
async def run_async():
    print("\n--- 2. Starting Async (All at once) ---")
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        # Prepare all 10 requests into tasks
        for i in range(1, REQUESTS_COUNT + 1):
            task = fetch_one(session, i)
            tasks.append(task)
        # Fire them all at the same time and wait for them to finish
        await asyncio.gather(*tasks)

    end = time.time()
    return end - start


time_sync = run_sync()

time_async = asyncio.run(run_async())

print("\n==============================")
print(f"Sync took:  {time_sync:.2f} seconds")
print(f"Async took: {time_async:.2f} seconds")
print("==============================")
