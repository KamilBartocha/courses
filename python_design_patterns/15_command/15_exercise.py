# 15_exercise.py - Command (Polecenie)

from abc import ABC, abstractmethod

# ─── Zadanie 1 ─ Urzadzenia smart home ────────────────────────────────────────
# TurnOnCommand(device), TurnOffCommand(device), SetTemperatureCommand(device, temp)
# SmartHome.execute(command), undo(), undo_all()

class SmartDevice:
    def __init__(self, name: str):
        self.name = name
        self._on = False
        self._temp = 20.0

    def turn_on(self) -> None: self._on = True; print(f'{self.name}: ON')
    def turn_off(self) -> None: self._on = False; print(f'{self.name}: OFF')
    def set_temp(self, temp: float) -> None: self._temp = temp; print(f'{self.name}: temp={temp}')
    def get_temp(self) -> float: return self._temp

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...

class TurnOnCommand(Command):
    def __init__(self, device: SmartDevice): self._device = device
    def execute(self) -> None: pass
    def undo(self) -> None: pass

class TurnOffCommand(Command):
    def __init__(self, device: SmartDevice): self._device = device
    def execute(self) -> None: pass
    def undo(self) -> None: pass

class SetTemperatureCommand(Command):
    def __init__(self, device: SmartDevice, temp: float):
        self._device = device; self._temp = temp; self._prev = 20.0
    def execute(self) -> None: pass
    def undo(self) -> None: pass

class SmartHome:
    def __init__(self): self._history: list[Command] = []
    def execute(self, command: Command) -> None: pass
    def undo(self) -> None: pass
    def undo_all(self) -> None: pass


home = SmartHome()
thermostat = SmartDevice('Thermostat')
lamp = SmartDevice('Lamp')

home.execute(TurnOnCommand(lamp))
home.execute(SetTemperatureCommand(thermostat, 22.0))
home.execute(TurnOffCommand(lamp))
print('Undo last:')
home.undo()
print('Undo all:')
home.undo_all()


# ─── Zadanie 2 ─ Kalkulator z historia ────────────────────────────────────────
# Calculator z history: add(n), sub(n), mul(n), div(n)
# Kazda operacja jako Command z undo()
# calc.undo() cofnie ostatnia operacje

class Calculator:
    def __init__(self): self._value = 0.0; self._history = []
    def execute(self, command: Command) -> None: pass
    def undo(self) -> None: pass
    @property
    def value(self) -> float: return self._value

class AddCommand(Command):
    def __init__(self, calc: Calculator, n: float): self._calc = calc; self._n = n
    def execute(self) -> None: pass
    def undo(self) -> None: pass

class MultiplyCommand(Command):
    def __init__(self, calc: Calculator, n: float): self._calc = calc; self._n = n
    def execute(self) -> None: pass
    def undo(self) -> None: pass


calc = Calculator()
calc.execute(AddCommand(calc, 10))
calc.execute(MultiplyCommand(calc, 3))
calc.execute(AddCommand(calc, 5))
print(f'Value: {calc.value}')  # (10 * 3) + 5 = 35
calc.undo()
print(f'After undo: {calc.value}')  # 30
calc.undo()
print(f'After undo: {calc.value}')  # 10


# ─── Zadanie 3 ─ Makro polecenie *(Trudniejsze)* ──────────────────────────────
# MacroCommand(commands: list) - wykonuje kilka polecen razem
# execute() -> wykonuje wszystkie; undo() -> cofa w odwrotnej kolejnosci

class MacroCommand(Command):
    def __init__(self, commands: list[Command]):
        self._commands = commands
    def execute(self) -> None:
        # hint: iteruj po commands i wywoluj execute()
        pass
    def undo(self) -> None:
        # hint: iteruj odwrotnie i wywoluj undo()
        pass


home2 = SmartHome()
light = SmartDevice('Living Room Light')
fan = SmartDevice('Fan')
heater = SmartDevice('Heater')

morning_routine = MacroCommand([
    TurnOnCommand(light),
    TurnOnCommand(fan),
    SetTemperatureCommand(heater, 21.0),
])

home2.execute(morning_routine)
print('After morning routine:')
print('Undoing morning routine:')
home2.undo()
