data = [1, 2, 3, [3, 4], 1, [5, 6]]

# [1, 2, 3, 3, 4, 1, 5, 6]

result = []
for element in data:
    if isinstance(element, int):
        result.append(element)
    if isinstance(element, list):
        for number in element:
            result.append(number)

print(result)
