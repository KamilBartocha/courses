# 07_exercise.py - Adapter

# ─── Zadanie 1 ─ Adapter obiektowy ────────────────────────────────────────────
# Stary interfejs: OldLogger.write_log(level: str, msg: str).
# Nowa biblioteka: StructuredLogger.log(payload: dict).
# Napisz StructuredLoggerAdapter implementujacy interfejs OldLogger.

class OldLogger:
    def write_log(self, level: str, msg: str) -> None:
        print(f'[{level}] {msg}')

class StructuredLogger:
    def log(self, payload: dict) -> None:
        print(f'STRUCTURED: {payload}')

class StructuredLoggerAdapter:
    def __init__(self, structured: StructuredLogger):
        pass

    def write_log(self, level: str, msg: str) -> None:
        pass


def log_event(logger: OldLogger, level: str, msg: str) -> None:
    logger.write_log(level, msg)

log_event(OldLogger(), 'ERROR', 'Connection failed')
log_event(StructuredLoggerAdapter(StructuredLogger()), 'ERROR', 'Connection failed')


# ─── Zadanie 2 ─ Adapter z __getattr__ ────────────────────────────────────────
# LegacyUserStore ma metody: find_by_id(id), save_user(user).
# Nowy interfejs: UserRepository.get(id), save(user), delete(id).
# Napisz adapter uzywajacy __getattr__ dla metod ktore nie sa
# przetlumaczone (przekaz bezposrednio do legacy).

class LegacyUserStore:
    def find_by_id(self, user_id: int) -> dict:
        return {'id': user_id, 'login': f'user{user_id}'}
    def save_user(self, user: dict) -> None:
        print(f'Legacy save: {user}')
    def find_all(self) -> list:
        return [{'id': 1}, {'id': 2}]  # metoda nie przetlumaczona

class UserRepositoryAdapter:
    def __init__(self, store: LegacyUserStore):
        pass

    def get(self, user_id: int) -> dict:
        pass

    def save(self, user: dict) -> None:
        pass

    def __getattr__(self, name: str):
        pass  # przekaz do legacy dla nieprzetlumaczonych metod


adapter = UserRepositoryAdapter(LegacyUserStore())
print(adapter.get(42))          # przetlumaczone
adapter.save({'id': 1})         # przetlumaczone
print(adapter.find_all())       # przekazane przez __getattr__


# ─── Zadanie 3 ─ Adapter CSV -> JSON ──────────────────────────────────────────
# CSVReader.read(path) -> list[list[str]] (wiersze jako listy stringow).
# JSONConsumer.consume(data: list[dict]) -> None.
# Adapter: CSVToJSONAdapter.consume(path) czyta CSV i podaje do consume.

class CSVReader:
    def read(self, path: str) -> list[list[str]]:
        # symulacja: zwraca naglowek + wiersze
        return [
            ['name', 'age', 'city'],
            ['Alice', '30', 'Warsaw'],
            ['Bob', '25', 'Krakow'],
        ]

class JSONConsumer:
    def consume(self, data: list[dict]) -> None:
        import json
        print(f'Consuming: {json.dumps(data, indent=2)}')

class CSVToJSONAdapter:
    def __init__(self, reader: CSVReader, consumer: JSONConsumer):
        pass

    def consume(self, path: str) -> None:
        pass


adapter = CSVToJSONAdapter(CSVReader(), JSONConsumer())
adapter.consume('data.csv')
# [{"name": "Alice", "age": "30", "city": "Warsaw"}, ...]


# ─── Zadanie 4 ─ Adapter dla zewnetrznej biblioteki ───────────────────────────
# Symuluj biblioteke zewnetrzna SmtpClient z metodami:
# connect(host, port), auth(user, pwd), send(from_, to, subject, body), quit().
# Napisz EmailService z prostym interfejsem send_email(to, subject, body)
# uzywajac adaptera wewnetrznie.

class SmtpClient:
    def connect(self, host: str, port: int) -> None:
        print(f'SMTP: connecting to {host}:{port}')
    def auth(self, user: str, pwd: str) -> None:
        print(f'SMTP: auth as {user}')
    def send(self, from_: str, to: str, subject: str, body: str) -> None:
        print(f'SMTP: sending "{subject}" from {from_} to {to}')
    def quit(self) -> None:
        print('SMTP: disconnected')

class EmailService:
    def __init__(self, host: str, port: int, user: str, pwd: str):
        self._smtp = SmtpClient()
        pass

    def send_email(self, to: str, subject: str, body: str) -> None:
        pass


svc = EmailService('mail.example.com', 587, 'bot@x.com', 'secret')
svc.send_email('alice@x.com', 'Hello!', 'Hi Alice!')


# ─── Zadanie 5 ─ Adapter dwukierunkowy *(Trudniejsze)* ───────────────────────
# MetricSystemSensor.measure() zwraca metry (float).
# ImperialSystemSensor.measure() zwraca stopy (float).
# Napisz MetricToImperialAdapter i ImperialToMetricAdapter.
# Napisz funkcje compare_heights(sensor_a, sensor_b) drukujaca
# obie wysokosci w metrach.
# # hint: 1 foot = 0.3048 meter

class MetricSensor:
    def measure(self) -> float:
        return 1.80  # metry

class ImperialSensor:
    def measure(self) -> float:
        return 6.0  # stopy

class MetricToImperialAdapter:
    def __init__(self, metric: MetricSensor):
        pass
    def measure(self) -> float:
        pass  # konwertuj metry -> stopy

class ImperialToMetricAdapter:
    def __init__(self, imperial: ImperialSensor):
        pass
    def measure(self) -> float:
        pass  # konwertuj stopy -> metry

def compare_heights(sensor_a: MetricSensor, sensor_b: MetricSensor) -> None:
    # obydwa sensory musza zwracac metry
    print(f'Sensor A: {sensor_a.measure():.2f}m')
    print(f'Sensor B: {sensor_b.measure():.2f}m')


metric = MetricSensor()
imperial_adapted = ImperialToMetricAdapter(ImperialSensor())
compare_heights(metric, imperial_adapted)
# Sensor A: 1.80m
# Sensor B: 1.83m
