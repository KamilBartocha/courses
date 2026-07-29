# 06_exercise.py - Prototype (Prototyp)

import copy

# ─── Zadanie 1 ─ Plasytka vs glęboka kopia ────────────────────────────────────
# Stworz obiekt Config z atrybutem `settings: dict`.
# Zrob plasytka kopie i zmien zagniezdzone dane.
# Pokaz roznice miedzy shallow i deep copy.

class Config:
    def __init__(self, settings: dict):
        self.settings = settings

    def __repr__(self) -> str:
        return f'Config({self.settings})'


cfg = Config({'db': {'host': 'localhost', 'port': 5432}, 'debug': True})
shallow = copy.copy(cfg)
deep = copy.deepcopy(cfg)

shallow.settings['db']['port'] = 9999  # zmienia tez oryginalna?
deep.settings['db']['host'] = 'prod.db'  # zmienia oryginalna?

print(f'Original:  {cfg}')
print(f'Shallow:   {shallow}')
print(f'Deep:      {deep}')


# ─── Zadanie 2 ─ __copy__ i __deepcopy__ ──────────────────────────────────────
# Zaimplementuj __copy__ i __deepcopy__ dla klasy DocumentTemplate.
# __copy__: wspoldzielony `styles` (dict), nowy `content` (list).
# __deepcopy__: wszystko skopiowane gleboko.

class DocumentTemplate:
    def __init__(self, title: str, styles: dict, content: list[str]):
        self.title = title
        self.styles = styles
        self.content = content

    def __copy__(self) -> 'DocumentTemplate':
        pass

    def __deepcopy__(self, memo: dict) -> 'DocumentTemplate':
        pass

    def __repr__(self) -> str:
        return f'Doc("{self.title}", styles={self.styles}, content={self.content})'


template = DocumentTemplate(
    'Report',
    {'font': 'Arial', 'size': 12},
    ['Introduction', 'Summary']
)

shallow_doc = copy.copy(template)
deep_doc = copy.deepcopy(template)

shallow_doc.title = 'Report Copy'
shallow_doc.styles['size'] = 14   # zmieni oryginalna? (shallow - tak)
deep_doc.styles['font'] = 'Times' # zmieni oryginalna? (deep - nie)

print(template)
print(shallow_doc)
print(deep_doc)


# ─── Zadanie 3 ─ Rejestr prototypow ──────────────────────────────────────────
# Zaimplementuj PrototypeRegistry.
# register(key, obj), clone(key) -> deepcopy.
# Rzuc KeyError gdy klucz nieznany.

class PrototypeRegistry:
    def __init__(self):
        self._registry: dict = {}

    def register(self, key: str, prototype) -> None:
        pass

    def clone(self, key: str):
        pass


registry = PrototypeRegistry()
registry.register('invoice', {'type': 'invoice', 'items': [], 'total': 0.0})
registry.register('receipt', {'type': 'receipt', 'items': [], 'paid': False})

inv1 = registry.clone('invoice')
inv2 = registry.clone('invoice')
inv1['items'].append({'name': 'Widget', 'price': 10.0})
inv2['items'].append({'name': 'Gadget', 'price': 25.0})

print(f'inv1: {inv1}')
print(f'inv2: {inv2}')  # niezalezna kopia - rozne items

try:
    registry.clone('unknown')
except KeyError as e:
    print(f'KeyError: {e}')


# ─── Zadanie 4 ─ Klonowanie gracza ────────────────────────────────────────────
# Napisz klase Player(name, level, inventory, stats).
# Zaimplementuj clone() zwracajacy glęboka kopie z nowym name.
# inventory i stats maja byc niezalezne od oryginalu.

class Player:
    def __init__(self, name: str, level: int,
                 inventory: list[str], stats: dict):
        self.name = name
        self.level = level
        self.inventory = inventory
        self.stats = stats

    def clone(self, new_name: str) -> 'Player':
        pass

    def __repr__(self) -> str:
        return f'Player({self.name}, lvl={self.level}, inv={self.inventory})'


hero = Player('Aragorn', 15, ['sword', 'shield'], {'str': 18, 'dex': 14})
twin = hero.clone('Boromir')
twin.inventory.append('bow')
twin.stats['str'] = 16

print(f'hero: {hero}')   # sword, shield - bez zmian
print(f'twin: {twin}')   # sword, shield, bow
print(f'hero.stats: {hero.stats}')  # str=18 - bez zmian


# ─── Zadanie 5 ─ Snapshot z prototypem *(Trudniejsze)* ───────────────────────
# Napisz klase Canvas z atrybutem shapes (list[dict]).
# Metoda snapshot() zapisuje deep copy do historii.
# Metoda undo() przywraca poprzedni snapshot.
# # hint: przechowuj liste historii jako stos (lista)

class Canvas:
    def __init__(self):
        self.shapes: list[dict] = []
        self._history: list[list[dict]] = []

    def add_shape(self, shape: dict) -> None:
        pass

    def snapshot(self) -> None:
        pass

    def undo(self) -> None:
        pass

    def __repr__(self) -> str:
        return f'Canvas({len(self.shapes)} shapes)'


canvas = Canvas()
canvas.add_shape({'type': 'circle', 'r': 10})
canvas.snapshot()
canvas.add_shape({'type': 'rect', 'w': 20, 'h': 15})
canvas.snapshot()
canvas.add_shape({'type': 'line', 'len': 50})
print(f'Before undo: {len(canvas.shapes)} shapes')  # 3
canvas.undo()
print(f'After undo:  {len(canvas.shapes)} shapes')  # 2
canvas.undo()
print(f'After undo2: {len(canvas.shapes)} shapes')  # 1
