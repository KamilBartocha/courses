# 04_cheat_sheet.py - Abstract Factory (Fabryka Abstrakcyjna)

from abc import ABC, abstractmethod


# ── Abstrakcyjne produkty ──────────────────────────────────────────────────────
class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...

class TextInput(ABC):
    @abstractmethod
    def render(self) -> str: ...

class Dialog(ABC):
    @abstractmethod
    def render(self) -> str: ...


# ── Konkretne produkty: motyw jasny ───────────────────────────────────────────
class LightButton(Button):
    def render(self) -> str: return "[Button: white bg]"

class LightTextInput(TextInput):
    def render(self) -> str: return "[Input: white bg]"

class LightDialog(Dialog):
    def render(self) -> str: return "[Dialog: white bg]"


# ── Konkretne produkty: motyw ciemny ──────────────────────────────────────────
class DarkButton(Button):
    def render(self) -> str: return "[Button: dark bg]"

class DarkTextInput(TextInput):
    def render(self) -> str: return "[Input: dark bg]"

class DarkDialog(Dialog):
    def render(self) -> str: return "[Dialog: dark bg]"


# ── Abstrakcyjna fabryka ──────────────────────────────────────────────────────
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...
    @abstractmethod
    def create_text_input(self) -> TextInput: ...
    @abstractmethod
    def create_dialog(self) -> Dialog: ...


# ── Konkretne fabryki ─────────────────────────────────────────────────────────
class LightThemeFactory(UIFactory):
    def create_button(self) -> Button: return LightButton()
    def create_text_input(self) -> TextInput: return LightTextInput()
    def create_dialog(self) -> Dialog: return LightDialog()

class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button: return DarkButton()
    def create_text_input(self) -> TextInput: return DarkTextInput()
    def create_dialog(self) -> Dialog: return DarkDialog()


# ── Klient uzywajacy fabryki ──────────────────────────────────────────────────
def render_login_screen(factory: UIFactory) -> None:
    btn = factory.create_button()
    inp = factory.create_text_input()
    dlg = factory.create_dialog()
    print(dlg.render())
    print(inp.render())
    print(btn.render())

render_login_screen(LightThemeFactory())
print("---")
render_login_screen(DarkThemeFactory())


# ── Fabryka wybierana z konfiguracji ─────────────────────────────────────────
def get_factory(theme: str) -> UIFactory:
    factories = {
        "light": LightThemeFactory,
        "dark": DarkThemeFactory,
    }
    if theme not in factories:
        raise ValueError(f"Unknown theme: {theme}")
    return factories[theme]()

factory = get_factory("dark")
factory.create_button().render()   # [Button: dark bg]
