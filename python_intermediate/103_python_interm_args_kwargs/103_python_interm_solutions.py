# Solutions: 103_python_interm_args_kwargs.ipynb
##############################################################################
# 1. multiply_all
##############################################################################

def multiply_all(*args):
    result = 1
    for value in args:
        result *= value
    return result


print(multiply_all(2, 3, 4))      # 24
print(multiply_all(1, 5, 2, 10))  # 100

##############################################################################
# 2. merge_lists
##############################################################################

def merge_lists(*args):
    result = []
    for lst in args:
        result.extend(lst)
    return result


print(merge_lists([1, 2], [3, 4], [5, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_lists([10], [20, 30]))           # [10, 20, 30]

##############################################################################
# 3. calculate_stats
##############################################################################

def calculate_stats(*args):
    return {
        'count':   len(args),
        'total':   sum(args),
        'average': round(sum(args) / len(args), 2),
        'minimum': min(args),
        'maximum': max(args),
    }


print(calculate_stats(4, 7, 2, 9, 1))
# {'count': 5, 'total': 23, 'average': 4.6, 'minimum': 1, 'maximum': 9}

##############################################################################
# 4. greet
##############################################################################

def greet(**kwargs):
    title = kwargs.get('title', '')
    name  = kwargs['name']
    full  = f"{title} {name}".strip() if title else name
    print(f"Hello, {full}!")


greet(name='Alice')              # Hello, Alice!
greet(name='Bob', title='Dr.')   # Hello, Dr. Bob!

##############################################################################
# 5. filter_params
##############################################################################

def filter_params(**kwargs):
    return {k: v for k, v in kwargs.items() if v > 10}


print(filter_params(a=5, b=15, c=25))       # {'b': 15, 'c': 25}
print(filter_params(x=1, y=100, z=11))      # {'y': 100, 'z': 11}

##############################################################################
# 6. validate_user
##############################################################################

def validate_user(**kwargs):
    required = ['name', 'email', 'age']
    for field in required:
        if field not in kwargs:
            print(f"Missing field: {field}")
            return
    print("User valid")


validate_user(name='Alice', email='alice@example.com', age=30)
# User valid
validate_user(name='Bob', age=25)
# Missing field: email

##############################################################################
# 7. format_message
##############################################################################

def format_message(*args, separator=', ', end='!'):
    return separator.join(args) + end


print(format_message('Hello', 'world'))              # Hello, world!
print(format_message('a', 'b', 'c',
                     separator=' - ', end='.'))       # a - b - c.

##############################################################################
# 8. build_html
##############################################################################

def build_html(tag, *content, **attributes):
    text  = ''.join(content)
    attrs = ' '.join(f'{k}="{v}"' for k, v in attributes.items())
    opening = f"<{tag} {attrs}>" if attrs else f"<{tag}>"
    return f"{opening}{text}</{tag}>"


print(build_html('p', 'Hello'))
# <p>Hello</p>
print(build_html('a', 'Click', href='http://example.com'))
# <a href="http://example.com">Click</a>

##############################################################################
# 9. log
##############################################################################

def log(level, *messages, **context):
    msg  = ' '.join(messages)
    ctx  = ' '.join(f"{k}={v}" for k, v in context.items())
    line = f"[{level}] {msg}"
    if ctx:
        line += f" | {ctx}"
    print(line)


log('INFO', 'Server', 'started', port=8080)
# [INFO] Server started | port=8080
log('ERROR', 'Connection', 'failed')
# [ERROR] Connection failed

##############################################################################
# 10. Łączenie słowników
##############################################################################

base   = {'host': 'localhost', 'port': 8080, 'debug': True}
custom = {'port': 9000, 'timeout': 30}

config = {**base, **custom}

print(config)
# {'host': 'localhost', 'port': 9000, 'debug': True, 'timeout': 30}

##############################################################################
# 11. Extended unpacking z posortowaną listą
##############################################################################

scores = [88, 72, 95, 60, 84]

worst, *rest, best = sorted(scores)

print(best)    # 95
print(worst)   # 60
print(rest)    # [72, 84, 88]

##############################################################################
# 12. Wywołanie funkcji przez rozpakowywanie
##############################################################################

def power(base, exponent, modulo=None):
    result = base ** exponent
    return result if modulo is None else result % modulo


args1 = [2, 10]
args2 = (3, 4)
args3 = {'base': 5, 'exponent': 3, 'modulo': 7}

print(power(*args1))   # 1024
print(power(*args2))   # 81
print(power(**args3))  # 6
