# 15_cheat_sheet.py - Command (Polecenie)

from abc import ABC, abstractmethod
from collections import deque
import queue


# ── Podstawowa implementacja ──────────────────────────────────────────────────
class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...

class TextEditor:
    def __init__(self) -> None:
        self._text = ''

    @property
    def text(self) -> str:
        return self._text

    def insert(self, text: str, pos: int) -> None:
        self._text = self._text[:pos] + text + self._text[pos:]

    def delete(self, pos: int, length: int) -> str:
        deleted = self._text[pos:pos + length]
        self._text = self._text[:pos] + self._text[pos + length:]
        return deleted

class InsertCommand(Command):
    def __init__(self, editor: TextEditor, text: str, pos: int):
        self._editor = editor
        self._text = text
        self._pos = pos

    def execute(self) -> None:
        self._editor.insert(self._text, self._pos)

    def undo(self) -> None:
        self._editor.delete(self._pos, len(self._text))

class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, pos: int, length: int):
        self._editor = editor
        self._pos = pos
        self._length = length
        self._deleted = ''

    def execute(self) -> None:
        self._deleted = self._editor.delete(self._pos, self._length)

    def undo(self) -> None:
        self._editor.insert(self._deleted, self._pos)

class CommandHistory:
    def __init__(self) -> None:
        self._history: list[Command] = []
        self._redo_stack: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self._history.append(command)
        self._redo_stack.clear()

    def undo(self) -> bool:
        if not self._history: return False
        cmd = self._history.pop()
        cmd.undo()
        self._redo_stack.append(cmd)
        return True

    def redo(self) -> bool:
        if not self._redo_stack: return False
        cmd = self._redo_stack.pop()
        cmd.execute()
        self._history.append(cmd)
        return True

editor = TextEditor()
history = CommandHistory()

history.execute(InsertCommand(editor, 'Hello', 0))
history.execute(InsertCommand(editor, ' World', 5))
history.execute(InsertCommand(editor, '!', 11))
print(editor.text)        # Hello World!
history.undo()
print(editor.text)        # Hello World
history.undo()
print(editor.text)        # Hello
history.redo()
print(editor.text)        # Hello World


# ── Kolejka polecen (Command Queue) ──────────────────────────────────────────
class LightCommand(Command):
    def __init__(self, name: str):
        self._name = name
        self._is_on = False

    def execute(self) -> None:
        self._is_on = True
        print(f'Light {self._name}: ON')

    def undo(self) -> None:
        self._is_on = False
        print(f'Light {self._name}: OFF')

class CommandQueue:
    def __init__(self) -> None:
        self._queue: queue.Queue = queue.Queue()

    def add(self, command: Command) -> None:
        self._queue.put(command)

    def run_all(self) -> None:
        while not self._queue.empty():
            command = self._queue.get()
            command.execute()

cmd_queue = CommandQueue()
cmd_queue.add(LightCommand('living_room'))
cmd_queue.add(LightCommand('kitchen'))
cmd_queue.add(LightCommand('bedroom'))
cmd_queue.run_all()
