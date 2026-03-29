import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open('05_file_text.txt', 'r')
print(f.name, f.mode)
f.close()

with open('05_file_text.txt', 'r') as f:
    content = f.read()
print(content[:80])

with open('05_file_text.txt', 'r') as f:
    lines = f.readlines()
print(f'Lines: {len(lines)}, last: {lines[-1].strip()}')

with open('output.txt', 'w') as f:
    f.write('Hello, Python!\n')
    f.write('Second line\n')

with open('output.txt', 'a') as f:
    f.write('Third line - appended\n')

with open('output.txt', 'r') as f:
    print(f.read())

import math
import math as m
from math import sqrt, pi

print(math.pi, m.floor(3.7), m.ceil(3.2), sqrt(25), pi)

import sys

print(os.getcwd())
print(f'Python {sys.version_info.major}.{sys.version_info.minor}')
print(f'Platform: {sys.platform}')
print(f"venv: {sys.prefix != sys.base_prefix}")
print(__name__)
