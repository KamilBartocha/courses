# 12_exercise.py - Bridge (Most)

from abc import ABC, abstractmethod

# ─── Zadanie 1 ─ Sterowniki urzadzen ──────────────────────────────────────────
# Device (ABC): power_on(), power_off(), set_channel(ch), set_volume(vol)
# TV(Device), Radio(Device)
# Remote(device): toggle_power(), channel_up(), volume_up()
# AdvancedRemote(device): mute()

class Device(ABC):
    @abstractmethod
    def power_on(self) -> None: ...
    @abstractmethod
    def power_off(self) -> None: ...
    @abstractmethod
    def set_channel(self, ch: int) -> None: ...
    @abstractmethod
    def set_volume(self, vol: int) -> None: ...
    @abstractmethod
    def is_on(self) -> bool: ...

class TV(Device):
    def __init__(self): self._on = False; self._ch = 1; self._vol = 50
    def power_on(self) -> None: self._on = True; print('TV on')
    def power_off(self) -> None: self._on = False; print('TV off')
    def set_channel(self, ch: int) -> None: self._ch = ch; print(f'TV ch={ch}')
    def set_volume(self, vol: int) -> None: self._vol = vol; print(f'TV vol={vol}')
    def is_on(self) -> bool: return self._on

class Radio(Device):
    def __init__(self): self._on = False; self._ch = 1; self._vol = 30
    def power_on(self) -> None: self._on = True; print('Radio on')
    def power_off(self) -> None: self._on = False; print('Radio off')
    def set_channel(self, ch: int) -> None: self._ch = ch; print(f'Radio ch={ch}')
    def set_volume(self, vol: int) -> None: self._vol = vol; print(f'Radio vol={vol}')
    def is_on(self) -> bool: return self._on

class Remote:
    def __init__(self, device: Device): self._device = device; self._ch = 1; self._vol = 50
    def toggle_power(self) -> None: pass
    def channel_up(self) -> None: pass
    def volume_up(self) -> None: pass

class AdvancedRemote(Remote):
    def mute(self) -> None: pass


tv_remote = Remote(TV())
tv_remote.toggle_power()
tv_remote.channel_up()
tv_remote.channel_up()
tv_remote.volume_up()

radio_remote = AdvancedRemote(Radio())
radio_remote.toggle_power()
radio_remote.mute()


# ─── Zadanie 2 ─ Eksport danych ───────────────────────────────────────────────
# DataExporter (ABC): export(data: list) -> str
# CSVExporter, JSONExporter, XMLExporter
# Report(exporter): generate(title, data) -> str
# SalesReport(exporter): generate_monthly(month, sales) -> str

class DataExporter(ABC):
    @abstractmethod
    def export(self, data: list) -> str: ...

class CSVExporter(DataExporter):
    def export(self, data: list) -> str:
        if not data: return ''
        header = ','.join(str(k) for k in data[0].keys())
        rows = '\n'.join(','.join(str(v) for v in row.values()) for row in data)
        return f'{header}\n{rows}'

class JSONExporter(DataExporter):
    def export(self, data: list) -> str:
        import json
        return json.dumps(data, indent=2)

class Report:
    def __init__(self, exporter: DataExporter):
        self._exporter = exporter
    def generate(self, title: str, data: list) -> str:
        pass

class SalesReport(Report):
    def generate_monthly(self, month: str, sales: list) -> str:
        pass


data = [{'product': 'Widget', 'qty': 10, 'total': 99.9}]
for exporter in [CSVExporter(), JSONExporter()]:
    report = Report(exporter)
    print(report.generate('Sales', data))
    print('---')


# ─── Zadanie 3 ─ Logowanie *(Trudniejsze)* ────────────────────────────────────
# LogHandler (ABC): emit(level, msg)
# ConsoleHandler, FileHandler, NetworkHandler
# Logger(handler): info(msg), warning(msg), error(msg)
# FormattedLogger(handler, format_func): formatuje przed emisja

class LogHandler(ABC):
    @abstractmethod
    def emit(self, level: str, msg: str) -> None: ...

class ConsoleHandler(LogHandler):
    def emit(self, level: str, msg: str) -> None:
        print(f'[{level}] {msg}')

class FileHandler(LogHandler):
    def __init__(self, filename: str): self._filename = filename
    def emit(self, level: str, msg: str) -> None:
        print(f'FILE({self._filename}): [{level}] {msg}')

class Logger:
    def __init__(self, handler: LogHandler): self._handler = handler
    def info(self, msg: str) -> None: pass
    def warning(self, msg: str) -> None: pass
    def error(self, msg: str) -> None: pass

class FormattedLogger(Logger):
    def __init__(self, handler: LogHandler, format_func):
        super().__init__(handler)
        self._format = format_func
    def info(self, msg: str) -> None: pass
    def warning(self, msg: str) -> None: pass
    def error(self, msg: str) -> None: pass


from datetime import datetime
ts_format = lambda level, msg: f'{datetime.now().strftime("%H:%M:%S")} {level}: {msg}'

log = FormattedLogger(ConsoleHandler(), ts_format)
log.info('Application started')
log.warning('Low memory')
log.error('Connection failed')
