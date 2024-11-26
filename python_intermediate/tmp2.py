# squares = [el ** 2 for el in range(10) if el % 2 == 0]
# print(squares)

# words = ["hello", "world", "python"]
# upper_words = [word.upper() for word in words]
# print(upper_words)

# def read_large_file(file_name):
#     with open(file_name, 'r') as file:
#         for line in file:
#             yield line.strip()

# for line in read_large_file('/Users/kamil/Repositories/jit-team-courses/python_intermediate/large_file.txt'):
#     print(line)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# even_odd = ['even' if x % 2 == 0 else 'odd' for x in range(1, 51)]

# sq = lambda x: x ** 2
# add = lambda *args: sum(args)


# print(add(2, 3))

# def sq2(x):
#     """"""
#     return x * 2

# multiply = lambda x, y: x * y
# print(multiply(4, 5))

# max_value = lambda x, y: x if x > y else y

# print(max_value(7, 10))

# is_even = lambda x: x % 2 == 0

# print(is_even(5))


# def last(x):
#     return x[-1]



# tuples = [(1, 3, 5), (4, 1, 1), (2, 2, 3)]
# sort1 = sorted(tuples, key=last)
# print(sort1)




# tuples3 = [(1, 3, 5), (4, 1, 1), (2, 2, 3)]
# sort3 = sorted(tuples, key=lambda x: x[-1])
# print(sort3)


# tuples3 = [[1, 3, 5], [4, 1, 1], [2, 2, 3]]
# sort3 = sorted([sorted(el) for el in tuples3], key=lambda x: x[1])
# print(sort3)


# list1 = [1, 2 ,3]
# func = lambda x: x * 2

# print(list(map(func, list1)))



# list2 = [1, 2 ,3]
# print(list(map(lambda x: x * 2, list2)))

# numbers1 = [1, 2, 3, 7]
# numbers2 = [4, 5, 6]
# summed_numbers = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(summed_numbers))




# list3 = [1, 2 , 3, 4, func, 3, '4']

# def filtr_mod_2(x):
#     return x % 2 == 0



# print(list(filter(lambda x: isinstance(x, int), list3)))

# def my_dec(funk):
#     def wrapper():
#         print('in wrapper')
#         funk()
#         print("po")
#     return wrapper


# def my_dec2(funk):
#     def wrapper():
#         print('in wrapper 2')
#         try:
#             funk()
#         except:
#             pass
#         print("po2")
#     return wrapper



# @my_dec
# def my_func():
#     print("my func")


# @my_dec
# def my_func2():
#     print("my func2")


# my_func()







# import time

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Czas wykonania: {end_time - start_time} sekundy")
#         return result
#     return wrapper


# @timing_decorator
# def slow_function(seconds):
#     time.sleep(seconds)
#     return "Gotowe!"


# print(slow_function(2))


# def greeting_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Start!')
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


# @greeting_decorator
# def say_hello(name):
#     return f"Hello, {name}!"


# print(say_hello("Mateusz"))

from datareader import ReadXML, ReadJSON

# Przykład użycia XML
xml_reader = ReadXML('example.xml')
xml_reader.load_xml()
print(xml_reader.get_value('root.item'))

# Przykład użycia JSON
json_reader = ReadJSON('example.json')
json_reader.load_json()
print(json_reader.get_value('item[0].value'))