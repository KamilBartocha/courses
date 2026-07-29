# 06_cheat_sheet.py - Prototype (Prototyp)

import copy
from typing import Optional


# ── Plasytka kopia (shallow copy) ─────────────────────────────────────────────
original = {'name': 'Alice', 'scores': [95, 87, 92]}
shallow = copy.copy(original)
shallow['name'] = 'Bob'          # niezalezna kopia
shallow['scores'].append(100)    # mutuje liste wspoldzielona!

print(original['name'])    # Alice (nie zmienione)
print(original['scores'])  # [95, 87, 92, 100] - wspoldzielona lista!


# ── Głęboka kopia (deep copy) ─────────────────────────────────────────────────
original2 = {'name': 'Alice', 'scores': [95, 87, 92]}
deep = copy.deepcopy(original2)
deep['scores'].append(100)

print(original2['scores'])  # [95, 87, 92] - bez zmian


# ── Klasa z __copy__ i __deepcopy__ ───────────────────────────────────────────
class GameCharacter:
    def __init__(self, name: str, hp: int, inventory: list[str]):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.history: list[str] = []

    def __copy__(self) -> 'GameCharacter':
        clone = GameCharacter(self.name, self.hp, self.inventory)
        # wspoldzielony inventory, nowa historia
        return clone

    def __deepcopy__(self, memo: dict) -> 'GameCharacter':
        clone = GameCharacter(
            self.name,
            self.hp,
            copy.deepcopy(self.inventory, memo),
        )
        clone.history = copy.deepcopy(self.history, memo)
        return clone

    def __repr__(self) -> str:
        return f'Character({self.name}, HP={self.hp}, items={self.inventory})'

hero = GameCharacter('Warrior', 100, ['sword', 'shield'])
hero.history.append('started game')

clone = copy.copy(hero)
deep_clone = copy.deepcopy(hero)

clone.name = 'Warrior2'
clone.inventory.append('potion')  # zmienia tez oryginalna!
print(f'hero:  {hero}')
print(f'clone: {clone}')

deep_clone.inventory.append('bow')  # nie zmienia oryginalnej
print(f'deep:  {deep_clone}')
print(f'hero:  {hero}')


# ── Rejestr prototypow ────────────────────────────────────────────────────────
class PrototypeRegistry:
    def __init__(self):
        self._prototypes: dict[str, GameCharacter] = {}

    def register(self, key: str, prototype: GameCharacter) -> None:
        self._prototypes[key] = prototype

    def clone(self, key: str) -> GameCharacter:
        prototype = self._prototypes.get(key)
        if prototype is None:
            raise KeyError(f'Unknown prototype: {key}')
        return copy.deepcopy(prototype)

registry = PrototypeRegistry()
registry.register('warrior', GameCharacter('Warrior', 100, ['sword']))
registry.register('mage', GameCharacter('Mage', 70, ['staff', 'spellbook']))

w1 = registry.clone('warrior')
w2 = registry.clone('warrior')
w1.name = 'ArthurWarrior'
w2.name = 'LancelotWarrior'
print(w1, w2)
