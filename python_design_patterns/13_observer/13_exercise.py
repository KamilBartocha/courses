# 13_exercise.py - Observer (Obserwator)

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

# ─── Zadanie 1 ─ System zdarzen ───────────────────────────────────────────────
# Napisz EventEmitter z metodami: on(event, handler), off(event, handler),
# emit(event, **data). Handler to Callable(**data) -> None.

class EventEmitter:
    def __init__(self):
        self._handlers: dict[str, list[Callable]] = {}

    def on(self, event: str, handler: Callable) -> None:
        pass

    def off(self, event: str, handler: Callable) -> None:
        pass

    def emit(self, event: str, **data) -> None:
        pass


emitter = EventEmitter()
log_click = lambda x, y, **kw: print(f'Click: ({x}, {y})')
emitter.on('click', log_click)
emitter.on('click', lambda x, y, **kw: print(f'Highlight at ({x}, {y})'))
emitter.emit('click', x=10, y=20)
emitter.off('click', log_click)
emitter.emit('click', x=30, y=40)  # tylko Highlight


# ─── Zadanie 2 ─ Monitor temperatury ─────────────────────────────────────────
# TemperatureSensor.set_temperature(temp) -> notifies all observers
# Observer interfejs: update(temp: float)
# Konkretne: HighTempAlert (> threshold), LowTempAlert (< threshold),
# TemperatureLogger (loguje kazda zmiane)

class TempObserver(ABC):
    @abstractmethod
    def update(self, temp: float) -> None: ...

class TemperatureSensor:
    def __init__(self):
        self._observers: list[TempObserver] = []
        self._temp = 20.0

    def subscribe(self, observer: TempObserver) -> None: pass
    def unsubscribe(self, observer: TempObserver) -> None: pass

    def set_temperature(self, temp: float) -> None:
        pass  # zmien i powiadom

class HighTempAlert(TempObserver):
    def __init__(self, threshold: float): self.threshold = threshold
    def update(self, temp: float) -> None: pass

class LowTempAlert(TempObserver):
    def __init__(self, threshold: float): self.threshold = threshold
    def update(self, temp: float) -> None: pass

class TemperatureLogger(TempObserver):
    def __init__(self): self.log = []
    def update(self, temp: float) -> None: pass


sensor = TemperatureSensor()
logger = TemperatureLogger()
sensor.subscribe(HighTempAlert(35.0))
sensor.subscribe(LowTempAlert(5.0))
sensor.subscribe(logger)

for temp in [20.0, 25.0, 37.0, 3.0, 22.0]:
    sensor.set_temperature(temp)

print('Log:', logger.log)


# ─── Zadanie 3 ─ Zdarzenia typowane *(Trudniejsze)* ──────────────────────────
# Napisz TypedEventBus z metodami:
# on(event_type: type, handler: Callable) -> None
# emit(event: object) -> None  (wysyla do handlerow dla type(event))
# Zdarzenia: UserLoginEvent(user), OrderCreatedEvent(order_id, amount)

@dataclass
class UserLoginEvent:
    user: str

@dataclass
class OrderCreatedEvent:
    order_id: int
    amount: float

class TypedEventBus:
    def __init__(self):
        self._handlers: dict[type, list[Callable]] = {}

    def on(self, event_type: type, handler: Callable) -> None:
        pass

    def emit(self, event) -> None:
        pass


bus = TypedEventBus()
bus.on(UserLoginEvent, lambda e: print(f'Login: {e.user}'))
bus.on(UserLoginEvent, lambda e: print(f'Audit: {e.user}'))
bus.on(OrderCreatedEvent, lambda e: print(f'Order {e.order_id}: {e.amount} PLN'))

bus.emit(UserLoginEvent('alice'))
bus.emit(OrderCreatedEvent(42, 99.99))
bus.emit(UserLoginEvent('bob'))
