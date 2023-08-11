power = lambda x, y: x ** y

print(power(2 ,4))

cw1 = lambda x: x
print(cw1(3))

cw2 = lambda x: x + 15
print(cw2(30))

cw3 = lambda x, y: x * y
print(cw3(4, 9))

subject_marks = [('Język angielski', 88),
                 ('Nauka',           90),
                 ('Matematyka',      97),
                 ('Nauki społeczne', 82)]

subject_marks.sort(key=lambda x: x[1])
print(subject_marks)

models = [{'marka': 'Nokia',   'model': '3310',   'kolor':    'Czarny'},
          {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
          {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]

sorted_models = sorted(models, key=lambda x: x["model"])

is_p_first_s = lambda s: True if s[0] == "p" else False
is_p_first_s2 = lambda s: True if s.startswith("p") else False

s = "pies"

print(is_p_first_s("kot"))
print(is_p_first_s2("pies"))

import datetime

now = datetime.datetime.now()

get_year = lambda x: x.year
get_month = lambda x: x.month
get_day = lambda x: x.day
get_time = lambda x: x.time


print(get_year(now))
print(get_month(now))
print(get_day(now))
print(get_time(now))

is_num = lambda x: x.replace(".", "", 1).isdigit()
print(is_num("-123"))



temperatury = [
    37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
    35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
    39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
    36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
    33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
    39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
    34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
    34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
    34.2, 40.2, 34.3, 35.3
]

# temp ponad 40

temp_ponad_40 = list(filter(lambda x: x >= 40, temperatury))
print(temp_ponad_40)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
odd_nums = list(filter(lambda y: y % 2 != 0, nums))

print(even_nums)
print(odd_nums)

array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]

result = list(filter(lambda x: x in array_nums1, array_nums2))
print(result)

array_nums = [1, 2, 3, 5, 7, 8, 9, 10]

even_nums = len(list(filter(lambda x: x % 2 == 0, array_nums)))
print(even_nums)

odd_nums = len(list(filter(lambda x: x % 2 == 1, array_nums)))
print(odd_nums)

weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']

len_6 = list(filter(lambda day: len(day) == 6, weekdays))
print(len_6)

nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

nums_19_or_13 = list(filter(lambda num: num % 19 == 0 or num % 13 == 0, nums))
print(nums_19_or_13)

texts = ["php", "w3rr3w", "Python", "abcd", "Java", "aaa"]

palindroms = list(filter(lambda text: text == "".join(reversed(text)) , texts))
print(palindroms)

text = "ala"


sample_names = ['antoni', 'Jakub', 'zuzanna', 'Julia', 'Jan', 'szymon']

sample_names_lower = list(filter(lambda name: name[0].isupper() == True, sample_names))
print(sample_names_lower)
print(len("".join(sample_names_lower)))

from statistics import mean
sr_temp = mean(temperatury)
print(sr_temp)

odch = list(map(lambda x: x - sr_temp, temperatury))
print(odch)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums_2_3 = list(map(lambda num: num ** 2, nums))
print(nums_2_3)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

added_nums = list(map(lambda x, y: x + y, nums1, nums2))
print(added_nums)

nums = [2, 4, 6, 9, 11]
n = 2

nums_multi = list(map(lambda x: x * n, nums))
print(nums_multi)

from functools import reduce
print(reduce(lambda x, y: x + y, nums))

fibb = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])
print(fibb(5))

def fib(n):
    return(reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1]))

print(fib(5))

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print(abs(sum([digit for digit in nums if digit < 0])))


array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
array_ordered = [x for x in array_nums if x < 0] + [y for y in array_nums if y >= 0]
print(array_ordered)

str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

print(sorted([int(x) for x in str1 if x.isdigit()]))
