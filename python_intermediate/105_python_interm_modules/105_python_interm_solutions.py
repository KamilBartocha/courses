# Solutions: 105_python_interm_own_modules.ipynb
##############################################################################
# 1. mathutils functions
##############################################################################

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def average(*args):
    return sum(args) / len(args)


print(add(3, 4))            # 7
print(subtract(10, 3))      # 7
print(multiply(3, 4))       # 12
print(average(1, 2, 3, 4))  # 2.5

##############################################################################
# 2. stringutils functions
##############################################################################

def clean(text):
    return text.strip()


def capitalize_words(text):
    return text.title()


def count_words(text):
    return len(text.split())


print(clean("  hello world  "))         # hello world
print(capitalize_words("hello world"))  # Hello World
print(count_words("one two three"))     # 3

##############################################################################
# 3. __init__.py dla pakietu myutils (strukturalne - jako komentarze)
##############################################################################

# myutils/__init__.py:
#
# from .mathutils import add, subtract, multiply, average
# from .stringutils import clean, capitalize_words, count_words
#
# Użytkownik importuje:
# from myutils import add, clean

##############################################################################
# 4. calculator/__init__.py (strukturalne - jako komentarze)
##############################################################################

# calculator/__init__.py:
#
# from .basic_ops import add, subtract, multiply
# from .advanced_ops import power, sqrt
#
# Użytkownik importuje:
# from calculator import add, subtract, multiply

##############################################################################
# 5. SimpleJSON
##############################################################################

import json


class SimpleJSON:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load(self):
        try:
            with open(self.file_path) as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error: {e}")

    def get(self, key):
        return self.data.get(key) if self.data else None


class SimpleJSONFromString(SimpleJSON):
    """Wersja testowa - wczytuje z napisu zamiast pliku."""
    def __init__(self, json_string):
        self.data = json.loads(json_string)
        self.file_path = None

    def load(self):
        pass


sample = '{"name": "Alice", "age": 30, "city": "Warsaw"}'
reader = SimpleJSONFromString(sample)
print(reader.get("name"))   # Alice
print(reader.get("age"))    # 30

##############################################################################
# 6. SimpleJSONExtended z keys() i summary()
##############################################################################

class SimpleJSONExtended(SimpleJSONFromString):
    def keys(self):
        return list(self.data.keys())

    def summary(self):
        for key, val in self.data.items():
            print(f"{key}: {type(val).__name__}")


sample2 = '{"name": "Alice", "age": 30, "scores": [95, 87]}'
reader2 = SimpleJSONExtended(sample2)
print(reader2.keys())   # ['name', 'age', 'scores']
reader2.summary()
# name: str
# age: int
# scores: list

##############################################################################
# 7. Testy unittest dla mathutils
##############################################################################

import unittest


class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)

    def test_average(self):
        self.assertEqual(average(1, 2, 3, 4), 2.5)
        self.assertEqual(average(10, 20), 15.0)


##############################################################################
# 8. Test obsługi błędu FileNotFoundError w ReadJSON
##############################################################################

import sys
sys.path.insert(0, '105_library/datareader')
from datareader.json_reader import ReadJSON


class TestReadJSONErrors(unittest.TestCase):
    def test_file_not_found(self):
        reader = ReadJSON('nonexistent_path.json')
        reader.load_json()
        self.assertIsNone(reader.data)


unittest.main(argv=[''], exit=False, verbosity=2)

##############################################################################
# 9. setup.py dla myutils (strukturalne - jako komentarze)
##############################################################################

# from setuptools import setup, find_packages
#
# setup(
#     name='myutils',
#     version='1.0.0',
#     description='Math and string utility functions',
#     packages=find_packages(),
#     python_requires='>=3.8',
# )
#
# Instalacja lokalna:
# pip install .
# pip install -e .   # tryb edytowalny (editable mode)
