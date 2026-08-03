# 11_cheat_sheet.py - Composite (Kompozyt)

from abc import ABC, abstractmethod


# ── Wspolny interfejs komponentu ──────────────────────────────────────────────
class FileSystemComponent(ABC):
    @abstractmethod
    def get_size(self) -> int: ...
    @abstractmethod
    def display(self, indent: int = 0) -> None: ...

class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self._size = size

    def get_size(self) -> int:
        return self._size

    def display(self, indent: int = 0) -> None:
        print(' ' * indent + f'📄 {self.name} ({self._size} B)')

class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self._children: list[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        self._children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        self._children.remove(component)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

    def display(self, indent: int = 0) -> None:
        print(' ' * indent + f'📁 {self.name}/ ({self.get_size()} B)')
        for child in self._children:
            child.display(indent + 2)


root = Directory('root')
docs = Directory('docs')
src = Directory('src')

docs.add(File('readme.md', 1024))
docs.add(File('spec.pdf', 51200))
src.add(File('main.py', 2048))
src.add(File('utils.py', 4096))
root.add(docs)
root.add(src)
root.add(File('config.json', 512))

root.display()
print(f'Total size: {root.get_size()} B')


# ── Composite menu restauracji ────────────────────────────────────────────────
class MenuComponent(ABC):
    @abstractmethod
    def get_price(self) -> float: ...
    @abstractmethod
    def describe(self, indent: int = 0) -> None: ...

class MenuItem(MenuComponent):
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    def get_price(self) -> float: return self._price

    def describe(self, indent: int = 0) -> None:
        print(' ' * indent + f'{self.name}: {self._price:.2f} PLN')

class Menu(MenuComponent):
    def __init__(self, name: str):
        self.name = name
        self._items: list[MenuComponent] = []

    def add(self, item: MenuComponent) -> None:
        self._items.append(item)

    def get_price(self) -> float:
        return sum(item.get_price() for item in self._items)

    def describe(self, indent: int = 0) -> None:
        print(' ' * indent + f'=== {self.name} ===')
        for item in self._items:
            item.describe(indent + 2)

drinks = Menu('Drinks')
drinks.add(MenuItem('Coffee', 8.0))
drinks.add(MenuItem('Tea', 6.0))

food = Menu('Food')
food.add(MenuItem('Soup', 12.0))
food.add(MenuItem('Sandwich', 15.0))

full_menu = Menu('Full Menu')
full_menu.add(drinks)
full_menu.add(food)
full_menu.describe()
print(f'Total: {full_menu.get_price():.2f} PLN')
