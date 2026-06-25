"""
Module 17 - pathlib solutions
"""
from pathlib import Path
from collections import defaultdict
import shutil


# Ćw. 1 - atrybuty Path
path = Path('/home/user/documents/report.final.pdf')
print(path.name)           # report.final.pdf
print(path.stem)           # report.final
print(path.suffix)         # .pdf
print(path.parent)         # /home/user/documents
print(path.parent.parent)  # /home/user


# Ćw. 2 - budowanie sciezki
config = Path('.') / 'settings' / 'dev' / 'config.json'
print(config)
print(config.exists())
print(config.resolve())


# Ćw. 3 - common_parent
def common_parent(paths: list[str]) -> Path:
    parts_list = [Path(p).parts for p in paths]
    common = []
    for parts in zip(*parts_list):
        if len(set(parts)) == 1:
            common.append(parts[0])
        else:
            break
    return Path(*common) if common else Path('/')


paths = ['/home/user/docs/report.pdf', '/home/user/docs/notes.txt', '/home/user/images/photo.jpg']
print(common_parent(paths))   # /home/user


# Ćw. 4 - path checks, cwd, home, mkdir
rel = Path('data/file.txt')
abs_p = Path('/tmp/file.txt')

print(rel.is_absolute())    # False
print(abs_p.is_absolute())  # True
print(Path('.').is_dir())   # True
print(Path('.').is_file())  # False
print(Path.cwd())
print(Path.home())

work = Path('temp_ex4') / 'a' / 'b'
work.mkdir(parents=True, exist_ok=True)
print(work.exists())   # True
print(work.is_dir())   # True
shutil.rmtree(Path('temp_ex4'))


# Ćw. 5 - count_lines
def count_lines(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding='utf-8').splitlines() if line.strip())


# Ćw. 6 - backup
def backup(path: Path) -> Path:
    bak = path.with_suffix('.bak' + path.suffix)
    bak.write_bytes(path.read_bytes())
    return bak


# Ćw. 7 - safe_write
def safe_write(path: Path, text: str) -> None:
    tmp = path.with_suffix('.tmp')
    try:
        tmp.write_text(text, encoding='utf-8')
        tmp.replace(path)
    except Exception:
        if tmp.exists():
            tmp.unlink()
        raise


# Ćw. 8 - shutil.copy + rename
src = Path('original.txt')
src.write_text('sample content', encoding='utf-8')

dst = Path('copy.txt')
shutil.copy(src, dst)
print(dst.read_text(encoding='utf-8'))   # sample content
print(dst.exists())                       # True

renamed = src.with_name('renamed.txt')
src.rename(renamed)
print(renamed.exists())   # True
print(src.exists())       # False

renamed.unlink()
dst.unlink()


# Ćw. 9 - list_files
def list_files(directory: Path, extension: str) -> list[str]:
    return sorted(p.name for p in directory.iterdir()
                  if p.is_file() and p.suffix == extension)


# Ćw. 10 - dir_size
def dir_size(directory: Path) -> int:
    return sum(f.stat().st_size for f in directory.rglob('*') if f.is_file())


# Ćw. 11 - find_duplicates
def find_duplicates(directory: Path) -> dict[int, list[Path]]:
    by_size: dict = defaultdict(list)
    for f in directory.rglob('*'):
        if f.is_file():
            by_size[f.stat().st_size].append(f)
    return {size: paths for size, paths in by_size.items() if len(paths) >= 2}


# Ćw. 12 - glob vs rglob
base = Path('temp_glob')
(base / 'sub').mkdir(parents=True, exist_ok=True)
for name in ('a.py', 'b.py', 'c.txt'):
    (base / name).write_text('', encoding='utf-8')
(base / 'sub' / 'd.py').write_text('', encoding='utf-8')

py_shallow = sorted(base.glob('*.py'))
print([p.name for p in py_shallow])   # ['a.py', 'b.py']

py_all = sorted(base.rglob('*.py'))
print([p.name for p in py_all])       # ['a.py', 'b.py', 'd.py']

shutil.rmtree(base)
