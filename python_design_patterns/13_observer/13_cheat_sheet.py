# 13_cheat_sheet.py - Observer (Obserwator)

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable
import logging


# ── Klasyczna implementacja ───────────────────────────────────────────────────
class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data: dict) -> None: ...

class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, event: str, data: dict) -> None:
        for obs in self._observers:
            obs.update(event, data)

class StockMarket(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._prices: dict[str, float] = {}

    def set_price(self, symbol: str, price: float) -> None:
        old = self._prices.get(symbol, 0)
        self._prices[symbol] = price
        if old != price:
            self.notify('price_changed', {'symbol': symbol, 'price': price, 'prev': old})

class StockAlert(Observer):
    def __init__(self, symbol: str, threshold: float) -> None:
        self._symbol = symbol
        self._threshold = threshold

    def update(self, event: str, data: dict) -> None:
        if data.get('symbol') == self._symbol and data['price'] < self._threshold:
            print(f'ALERT: {self._symbol} dropped below {self._threshold}: {data["price"]}')

market = StockMarket()
market.subscribe(StockAlert('AAPL', 150.0))
market.subscribe(StockAlert('GOOG', 100.0))
market.set_price('AAPL', 155.0)
market.set_price('AAPL', 148.0)  # trigger alert
market.set_price('GOOG', 105.0)


# ── Observer z Callable (funkcja jako observer) ───────────────────────────────
class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable]] = {}

    def on(self, event: str, handler: Callable) -> None:
        self._handlers.setdefault(event, []).append(handler)

    def emit(self, event: str, **data) -> None:
        for handler in self._handlers.get(event, []):
            handler(**data)

bus = EventBus()
bus.on('user.login', lambda user, **kw: print(f'Login: {user}'))
bus.on('user.login', lambda user, **kw: print(f'Audit: {user} logged in'))
bus.on('order.created', lambda order_id, **kw: print(f'Order {order_id} created'))
bus.emit('user.login', user='alice')
bus.emit('order.created', order_id=42)


# ── Zdarzenia jako dataclasses ────────────────────────────────────────────────
@dataclass
class Event:
    name: str
    data: dict

@dataclass
class PriceChangedEvent(Event):
    symbol: str
    price: float
    prev_price: float

    def __init__(self, symbol: str, price: float, prev: float):
        super().__init__('price_changed', {})
        self.symbol = symbol; self.price = price; self.prev_price = prev

class TypedEventBus:
    def __init__(self) -> None:
        self._handlers: dict[type, list[Callable]] = {}

    def on(self, event_type: type, handler: Callable) -> None:
        self._handlers.setdefault(event_type, []).append(handler)

    def emit(self, event: Event) -> None:
        for handler in self._handlers.get(type(event), []):
            handler(event)

typed_bus = TypedEventBus()
typed_bus.on(PriceChangedEvent, lambda e: print(f'{e.symbol}: {e.prev_price} -> {e.price}'))
typed_bus.emit(PriceChangedEvent('AAPL', 155.0, 148.0))


# ── logging jako Observer ─────────────────────────────────────────────────────
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logger.addHandler(handler)
logger.info('Observer example: logging module uses Observer pattern')
