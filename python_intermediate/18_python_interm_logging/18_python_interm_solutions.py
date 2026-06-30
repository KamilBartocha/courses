"""
Module 18 - logging solutions
"""
import logging
import uuid
from collections import deque
from functools import wraps
from logging.handlers import RotatingFileHandler
import os


# Ćw. 1 - basicConfig i 5 poziomow
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logging.debug('Szczegol diagnostyczny')
logging.info('Aplikacja wystartowała')
logging.warning('Ostrzezenie')
logging.error('Blad')
logging.critical('Blad krytyczny')


# Ćw. 2 - safe_divide z logowaniem
def safe_divide(a, b):
    if b == 0:
        logging.error('Dzielenie przez zero: %s / %s', a, b)
        return None
    result = a / b
    if result > 1000:
        logging.warning('Duzy wynik: %s / %s = %s', a, b, result)
    else:
        logging.debug('safe_divide(%s, %s) = %s', a, b, result)
    return result


# Ćw. 3 - dekorator log_calls
def log_calls(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.debug('Wywolanie %s(%s)', func.__name__, args)
            try:
                result = func(*args, **kwargs)
                logger.debug('%s -> %s', func.__name__, result)
                return result
            except Exception as e:
                logger.error('%s zglosil wyjatek: %s', func.__name__, e)
                raise
        return wrapper
    return decorator


# Ćw. 4 - logging.exception()
def parse_int(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        logging.exception('Nie mozna sparsowac jako int: %r', text)
        return None


# Ćw. 5 - logger z dwoma handlerami
def setup_audit_logger():
    audit = logging.getLogger('audit')
    audit.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    fh = logging.FileHandler('audit.log', encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    audit.addHandler(ch)
    audit.addHandler(fh)
    return audit


# Ćw. 6 - get_logger
def get_logger(name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    ch.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    fh = logging.FileHandler(log_file, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger


# Ćw. 7 - InMemoryHandler
class InMemoryHandler(logging.Handler):
    def __init__(self, capacity: int = 100):
        super().__init__()
        self.records: deque = deque(maxlen=capacity)

    def emit(self, record: logging.LogRecord) -> None:
        self.records.append(self.format(record))

    def get_records(self) -> list[str]:
        return list(self.records)


# Ćw. 8 - RotatingFileHandler
def setup_rotating_logger(log_file: str) -> logging.Logger:
    rot_logger = logging.getLogger('rotating')
    rot_logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=1024, backupCount=3)
    handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    rot_logger.addHandler(handler)
    return rot_logger


# Ćw. 9 - hierarchia loggerow
# service.setLevel(logging.WARNING)
# service_db.setLevel(logging.DEBUG)
# service_db.debug widoczny (override), service_api.info nie (dziedziczy WARNING)


# Ćw. 10 - DatabaseService
class DatabaseService:
    def __init__(self, dsn: str):
        self._logger = logging.getLogger(__name__)
        self._dsn = dsn

    def connect(self) -> None:
        self._logger.info('Connecting to %s', self._dsn)

    def query(self, sql: str) -> list:
        self._logger.debug('Query: %s', sql)
        return []

    def disconnect(self) -> None:
        self._logger.info('Disconnected')


# Ćw. 11 - RequestFilter
class RequestFilter(logging.Filter):
    def __init__(self, request_id: str):
        super().__init__()
        self.request_id = request_id

    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = self.request_id
        return True


# Ćw. 12 - NullHandler library pattern
LIB_LOGGER_NAME = 'mylib'

# Strona biblioteki: cicha domyslnie
logging.getLogger(LIB_LOGGER_NAME).addHandler(logging.NullHandler())


class MyLibrary:
    def __init__(self):
        self._logger = logging.getLogger(LIB_LOGGER_NAME)

    def do_work(self) -> None:
        self._logger.info('MyLibrary: praca w toku')
        self._logger.debug('MyLibrary: szczegól')


# Strona aplikacji: podlacza handler gdy potrzebuje logow biblioteki
def enable_library_logging() -> None:
    lib_logger = logging.getLogger(LIB_LOGGER_NAME)
    lib_logger.setLevel(logging.DEBUG)
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter('%(name)s | %(levelname)s | %(message)s'))
    lib_logger.addHandler(h)
