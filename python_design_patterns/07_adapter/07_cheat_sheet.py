# 07_cheat_sheet.py - Adapter

# ── Problem: niezgodnosc interfejsow ─────────────────────────────────────────
# Stary kod uzywa metody old_interface.get_data()
# Nowa biblioteka uzywa metody new_lib.fetch()
# Adapter tlUmaczy jeden na drugi.


# ── Adapter obiektowy (kompozycja) ────────────────────────────────────────────
class OldPaymentGateway:
    def make_payment(self, amount: float, currency: str) -> dict:
        return {'status': 'ok', 'amount': amount, 'currency': currency}

class NewPaymentGateway:
    def process(self, payload: dict) -> bool:
        print(f'NewGW: processing {payload}')
        return True

class NewGatewayAdapter:
    def __init__(self, new_gw: NewPaymentGateway):
        self._gw = new_gw            # kompozycja

    def make_payment(self, amount: float, currency: str) -> dict:
        payload = {'amount': amount, 'currency': currency}
        success = self._gw.process(payload)
        return {'status': 'ok' if success else 'error',
                'amount': amount, 'currency': currency}

def checkout(gateway: OldPaymentGateway, amount: float) -> None:
    result = gateway.make_payment(amount, 'PLN')
    print(f'Payment: {result}')

checkout(OldPaymentGateway(), 49.99)
checkout(NewGatewayAdapter(NewPaymentGateway()), 49.99)


# ── Adapter klasowy (wielodziedziczenie) ──────────────────────────────────────
class XMLParser:
    def parse_xml(self, xml: str) -> list[dict]:
        return [{'tag': 'item', 'text': xml}]

class JSONOutput:
    def to_json(self, data: list[dict]) -> str:
        import json
        return json.dumps(data)

class XMLToJSONAdapter(JSONOutput, XMLParser):
    def to_json(self, xml_string: str) -> str:
        data = self.parse_xml(xml_string)
        import json
        return json.dumps(data)

adapter = XMLToJSONAdapter()
print(adapter.to_json('<items><item>Widget</item></items>'))


# ── __getattr__ jako adapter dynamiczny ───────────────────────────────────────
class LegacyAPI:
    def get_user_info(self, user_id: int) -> dict:
        return {'id': user_id, 'user_name': 'alice', 'e_mail': 'alice@x.com'}

class ModernAPIAdapter:
    def __init__(self, legacy: LegacyAPI):
        self._legacy = legacy

    def __getattr__(self, name: str):
        return getattr(self._legacy, name)

    def get_user(self, user_id: int) -> dict:
        raw = self._legacy.get_user_info(user_id)
        return {
            'id': raw['id'],
            'username': raw['user_name'],
            'email': raw['e_mail'],
        }

adapter = ModernAPIAdapter(LegacyAPI())
print(adapter.get_user(42))    # nowoczesny interfejs
