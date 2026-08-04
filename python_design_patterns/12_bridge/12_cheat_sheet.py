# 12_cheat_sheet.py - Bridge (Most)

from abc import ABC, abstractmethod


# ── Implementor (interfejs implementacji) ─────────────────────────────────────
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, x: int, y: int, radius: int) -> None: ...
    @abstractmethod
    def render_rectangle(self, x: int, y: int, w: int, h: int) -> None: ...

class VectorRenderer(Renderer):
    def render_circle(self, x, y, radius) -> None:
        print(f'SVG <circle cx="{x}" cy="{y}" r="{radius}"/>')
    def render_rectangle(self, x, y, w, h) -> None:
        print(f'SVG <rect x="{x}" y="{y}" width="{w}" height="{h}"/>')

class RasterRenderer(Renderer):
    def render_circle(self, x, y, radius) -> None:
        print(f'PNG draw_circle({x}, {y}, r={radius})')
    def render_rectangle(self, x, y, w, h) -> None:
        print(f'PNG draw_rect({x}, {y}, {w}x{h})')


# ── Abstraction (interfejs abstrakcji) ────────────────────────────────────────
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer  # Most (Bridge) do implementacji

    @abstractmethod
    def draw(self) -> None: ...
    @abstractmethod
    def resize(self, factor: float) -> None: ...

class Circle(Shape):
    def __init__(self, renderer: Renderer, x: int, y: int, radius: int):
        super().__init__(renderer)
        self.x = x; self.y = y; self.radius = radius

    def draw(self) -> None:
        self.renderer.render_circle(self.x, self.y, self.radius)

    def resize(self, factor: float) -> None:
        self.radius = int(self.radius * factor)

class Rectangle(Shape):
    def __init__(self, renderer: Renderer, x: int, y: int, w: int, h: int):
        super().__init__(renderer)
        self.x = x; self.y = y; self.w = w; self.h = h

    def draw(self) -> None:
        self.renderer.render_rectangle(self.x, self.y, self.w, self.h)

    def resize(self, factor: float) -> None:
        self.w = int(self.w * factor); self.h = int(self.h * factor)


# Mozna laczyc dowolne ksztalty z dowolnymi rendererami
for renderer in [VectorRenderer(), RasterRenderer()]:
    print(f'\n--- {type(renderer).__name__} ---')
    Circle(renderer, 5, 5, 10).draw()
    Rectangle(renderer, 0, 0, 100, 50).draw()


# ── Bridge dla notyfikacji ────────────────────────────────────────────────────
class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None: ...

class EmailSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f'Email to {recipient}: {message}')

class SMSSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f'SMS to {recipient}: {message[:160]}')

class Notification(ABC):
    def __init__(self, sender: MessageSender):
        self._sender = sender
    @abstractmethod
    def notify(self, user: str, event: str) -> None: ...

class AlertNotification(Notification):
    def notify(self, user: str, event: str) -> None:
        self._sender.send(user, f'ALERT: {event}')

class InfoNotification(Notification):
    def notify(self, user: str, event: str) -> None:
        self._sender.send(user, f'INFO: {event}')

AlertNotification(EmailSender()).notify('alice@x.com', 'Login from new device')
InfoNotification(SMSSender()).notify('+48123', 'Your order shipped')
