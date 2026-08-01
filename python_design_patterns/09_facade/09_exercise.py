# 09_exercise.py - Facade (Fasada)

# ─── Zadanie 1 ─ Prosta fasada ────────────────────────────────────────────────
# Podsystem zamawiania jedzenia sklada sie z:
# MenuService.get_items() -> list[dict]
# OrderService.create_order(items) -> str (order_id)
# PaymentService.charge(order_id, amount) -> bool
# DeliveryService.schedule(order_id) -> str (eta)
# Napisz FoodOrderFacade.order(item_names: list[str]) laczaca wszystkie.

class MenuService:
    def get_items(self) -> list[dict]:
        return [
            {'name': 'Pizza', 'price': 35.0},
            {'name': 'Burger', 'price': 22.0},
            {'name': 'Salad', 'price': 18.0},
        ]

class OrderService:
    def create_order(self, items: list[dict]) -> str:
        print(f'Order created: {[i["name"] for i in items]}')
        return 'ORD-001'

class PaymentService:
    def charge(self, order_id: str, amount: float) -> bool:
        print(f'Charged {amount:.2f} PLN for {order_id}')
        return True

class DeliveryService:
    def schedule(self, order_id: str) -> str:
        return '30 minutes'

class FoodOrderFacade:
    def __init__(self):
        pass

    def order(self, item_names: list[str]) -> str:
        pass


facade = FoodOrderFacade()
eta = facade.order(['Pizza', 'Salad'])
print(f'ETA: {eta}')


# ─── Zadanie 2 ─ Fasada dla systemu plikow ────────────────────────────────────
# Podsystem: FileReader.read(path) -> str,
# TextParser.parse(text) -> list[dict],
# DataValidator.validate(data) -> bool,
# DataStorage.store(data) -> None.
# Fasada: FileImportFacade.import_file(path) -> int (liczba rekordow).

class FileReader:
    def read(self, path: str) -> str:
        return 'name,age\nAlice,30\nBob,25'

class TextParser:
    def parse(self, text: str) -> list[dict]:
        lines = text.strip().split('\n')
        headers = lines[0].split(',')
        return [dict(zip(headers, row.split(','))) for row in lines[1:]]

class DataValidator:
    def validate(self, data: list[dict]) -> bool:
        return all('name' in row for row in data)

class DataStorage:
    def __init__(self): self.records: list[dict] = []
    def store(self, data: list[dict]) -> None:
        self.records.extend(data)

class FileImportFacade:
    def __init__(self, storage: DataStorage):
        pass

    def import_file(self, path: str) -> int:
        pass


storage = DataStorage()
facade = FileImportFacade(storage)
count = facade.import_file('users.csv')
print(f'Imported: {count} records')
print(f'Storage: {storage.records}')


# ─── Zadanie 3 ─ Wielokrotna fasada ──────────────────────────────────────────
# Napisz HomeAutomationFacade laczaca:
# LightSystem.turn_on_all(), LightSystem.turn_off_all()
# ClimateSystem.set_temperature(t), ClimateSystem.get_temperature() -> float
# SecuritySystem.arm(), SecuritySystem.disarm()
# Metody fasady: leave_home(), arrive_home(), sleep_mode().

class LightSystem:
    def turn_on_all(self): print('Lights: ON')
    def turn_off_all(self): print('Lights: OFF')
    def dim(self, pct: int): print(f'Lights: {pct}%')

class ClimateSystem:
    def set_temperature(self, t: float): print(f'Temp: {t}C')
    def get_temperature(self) -> float: return 21.0
    def off(self): print('Climate: OFF')

class SecuritySystem:
    def arm(self): print('Security: ARMED')
    def disarm(self): print('Security: DISARMED')

class HomeAutomationFacade:
    def __init__(self):
        pass

    def leave_home(self) -> None:
        pass  # gasnij swiatla, ustaw 18C, uzbroj alarm

    def arrive_home(self) -> None:
        pass  # wlacz swiatla, ustaw 22C, rozbrojenie

    def sleep_mode(self) -> None:
        pass  # przyciemnij 10%, ustaw 19C, uzbroj alarm


facade = HomeAutomationFacade()
print('--- Leaving home ---')
facade.leave_home()
print('--- Arriving home ---')
facade.arrive_home()
print('--- Sleep mode ---')
facade.sleep_mode()


# ─── Zadanie 4 ─ Facade vs Adapter ───────────────────────────────────────────
# Uzupelnij komentarze: ktory to Facade, ktory Adapter, i dlaczego?

class OldMailer:
    def send_mail(self, to: str, subj: str, body: str): ...

class NewMailer:
    def compose(self, msg: dict): ...

# Klasa A
class MailerA:
    def __init__(self, old: OldMailer): self._old = old
    def compose(self, msg: dict):
        self._old.send_mail(msg['to'], msg['subject'], msg['body'])

# Klasa B
class MailerB:
    def __init__(self):
        self._smtp = OldMailer()
        self._template = object()   # TemplateEngine

    def send_welcome_email(self, user: str) -> None:
        self._smtp.send_mail(user, 'Welcome!', 'Hello!')

    def send_invoice(self, user: str, amount: float) -> None:
        self._smtp.send_mail(user, 'Invoice', f'Amount: {amount}')

print('MailerA to: Adapter (zmienia interfejs OldMailer na interfejs NewMailer)')
print('MailerB to: Facade (upraszcza podsystem do prostych operacji wysokiego poziomu)')


# ─── Zadanie 5 ─ Fasada API *(Trudniejsze)* ──────────────────────────────────
# Napisz APIClientFacade dla HTTP API.
# Podsystemy: AuthService(token), RequestBuilder, ResponseParser.
# Fasada: get(endpoint), post(endpoint, data), get_paged(endpoint, pages).
# # hint: get_paged wywoluje get() wielokrotnie z ?page=N

class AuthService:
    def __init__(self, token: str): self.token = token
    def get_headers(self) -> dict: return {'Authorization': f'Bearer {self.token}'}

class RequestBuilder:
    def build_get(self, url: str, headers: dict) -> dict:
        return {'method': 'GET', 'url': url, 'headers': headers}
    def build_post(self, url: str, headers: dict, data: dict) -> dict:
        return {'method': 'POST', 'url': url, 'headers': headers, 'body': data}

class ResponseParser:
    def parse(self, response: dict) -> dict:
        return {'status': 200, 'data': response}

class APIClientFacade:
    BASE_URL = 'https://api.example.com'

    def __init__(self, token: str):
        pass

    def get(self, endpoint: str) -> dict:
        pass

    def post(self, endpoint: str, data: dict) -> dict:
        pass

    def get_paged(self, endpoint: str, pages: int) -> list[dict]:
        pass


client = APIClientFacade('my-token-123')
print(client.get('/users'))
print(client.post('/users', {'name': 'Alice'}))
results = client.get_paged('/products', pages=3)
print(f'Pages fetched: {len(results)}')
