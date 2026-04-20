# Notebook Rules — Python Basics

## Language & typography

- Theory/prose cells: Polish, academic "we" voice
  - `wywołujemy` not `wywołujesz`, `definiujemy` not `definiujesz`,
    `możemy` not `możesz`, `tworzymy` not `tworzysz`
- Code cells: English variable names and string literals
  - `list1`, `cubes`, `text` — not `lista1`, `szesciany`, `tekst`
  - `"alice"` not `"ala"`
- Inline code snippets in markdown must match the code cells
- Technical terms: Polish first, English in brackets
  - `klasa (class)`, `metoda (method)`, `dziedziczenie (inheritance)`
- Max 79 characters per text line
- Use `-` (hyphen), not `—` (em dash)

## Cell structure

Every section follows this order — no exceptions:

```
## N. 🔹 Section name
Theory cell(s)     — Polish prose
Example code cell  — English variable names, runnable
---
### 🐍 Ćwiczenia — topic
One markdown cell listing all exercises
One code cell per exercise
```

## Notebook layout

```
# Title  (single # header, version 2.0, author name)
Rozkład jazdy  (agenda cell — one emoji-prefixed line per section)
---
[sections in order]
```

- Numbered sections: `## 1.`, `## 2.`, …
- One emoji per section header
- Merge thin one-liner cells into neighbours
- No duplicate headers after separators

## Theory cells

- Readable prose, not bullet-point dumps
- Key terms defined with concrete examples
- `> 💡` blockquotes for gotchas and practical advice
- `⚠️` callouts for surprising beginner behaviour
  (always with a runnable example)
- Comparison tables (`| | Option A | Option B |`) to contrast concepts
- Every concept appears before it is used in an exercise

## Example cells

- One focused, runnable cell per concept
- English variable names throughout

## Exercise cells

- Input data and variable names pre-defined
- `...` as the placeholder for the student solution
- Always ends with `print()` so output is visible
- `# hint:` comment on harder exercises
- Marked with `*(Trudniejsze)*` for hard difficulty
- Minimum 3 exercises per section: easy → medium → hard
- If a section introduces N distinct concepts/methods, provide at least N exercises
  so every introduced concept is covered by at least one exercise
- No exercise uses a concept taught in a later section
- Dict comprehension exercises: use `.items()` explicitly in the template
