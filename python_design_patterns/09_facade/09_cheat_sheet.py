# 09_cheat_sheet.py - Facade (Fasada)


# ── Podsystemy ────────────────────────────────────────────────────────────────
class VideoDecoder:
    def decode(self, filename: str) -> str:
        print(f'Decoding video: {filename}')
        return f'decoded:{filename}'

class AudioDecoder:
    def decode(self, filename: str) -> str:
        print(f'Decoding audio: {filename}')
        return f'audio:{filename}'

class VideoRenderer:
    def render(self, video_data: str) -> None:
        print(f'Rendering: {video_data}')

class AudioRenderer:
    def play(self, audio_data: str) -> None:
        print(f'Playing: {audio_data}')

class SubtitleLoader:
    def load(self, filename: str) -> str:
        return f'subtitles:{filename}'


# ── Fasada ────────────────────────────────────────────────────────────────────
class VideoPlayerFacade:
    def __init__(self) -> None:
        self._video_dec = VideoDecoder()
        self._audio_dec = AudioDecoder()
        self._video_ren = VideoRenderer()
        self._audio_ren = AudioRenderer()
        self._subtitles = SubtitleLoader()

    def play(self, filename: str, subtitles: bool = False) -> None:
        print(f'--- Playing {filename} ---')
        video = self._video_dec.decode(filename)
        audio = self._audio_dec.decode(filename)
        if subtitles:
            subs = self._subtitles.load(filename + '.srt')
            print(f'Subtitles loaded: {subs}')
        self._video_ren.render(video)
        self._audio_ren.play(audio)
        print('--- Done ---')

# Klient uzywa tylko fasady
player = VideoPlayerFacade()
player.play('movie.mp4', subtitles=True)


# ── Fasada dla podsystemu bazy danych ────────────────────────────────────────
class ConnectionPool:
    def get_connection(self) -> str:
        return 'conn:1'
    def release(self, conn: str) -> None:
        pass

class QueryExecutor:
    def execute(self, conn: str, sql: str) -> list:
        return [{'id': 1, 'name': 'Alice'}]

class ResultMapper:
    def map(self, rows: list, cls: type) -> list:
        return [cls(**row) for row in rows]

class DatabaseFacade:
    def __init__(self) -> None:
        self._pool = ConnectionPool()
        self._executor = QueryExecutor()
        self._mapper = ResultMapper()

    def query(self, sql: str, model_class: type = dict) -> list:
        conn = self._pool.get_connection()
        try:
            rows = self._executor.execute(conn, sql)
            if model_class is dict:
                return rows
            return self._mapper.map(rows, model_class)
        finally:
            self._pool.release(conn)

db = DatabaseFacade()
print(db.query('SELECT * FROM users'))
