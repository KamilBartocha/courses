import sys
import platform
import importlib.util
import math

print(sys.version)
print(sys.executable)
print(f"Python {sys.version_info.major}.{sys.version_info.minor}")

print(platform.system())
print(platform.architecture()[0])

for module in ["numpy", "pandas", "requests"]:
    found = importlib.util.find_spec(module) is not None
    print(f"{module:15} {'dostępny' if found else 'niedostępny'}")

print("Hello, World!")

name = "Alice"
print(f"Cześć, {name}!")

for i in range(1, 4):
    print(f"7 × {i} = {7 * i}")

radius = 5
print(f"Pole koła: {math.pi * radius ** 2:.2f}")

def calculate_bmi(weight: float, height: float) -> float:
    """Oblicz BMI."""
    return weight / (height ** 2)

print(f"BMI: {calculate_bmi(70, 1.75):.1f}")
