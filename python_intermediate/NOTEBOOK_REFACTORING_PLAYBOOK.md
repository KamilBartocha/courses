# Notebook Refactoring Playbook

## Instructions — apply to any Python intermediate notebook

### 1. Translate code examples to English
- Rename all Polish variable names to English equivalents
  - `lista1` → `list1`, `szesciany` → `cubes`, `tekst` → `text`, etc.
- Translate string literals inside code (`"ala"` → `"alice"`)
- Update inline code snippets inside markdown cells to match

### 2. Improve theory explanations
- Rewrite bullet-point dumps into readable prose
- Define key terms with concrete examples, not just definitions
- Add `> 💡` tip blockquotes for gotchas and practical advice

### 3. Structure each section as: Theory → Example → Exercises
- **Theory:** explain the concept in plain language
- **Example:** runnable code cell demonstrating the concept
- **Visual separator** (`---`) between theory and exercises
- **Exercises:** all descriptions in one markdown cell,
  then one code cell per exercise

### 4. Add exercises with code templates
- Each exercise gets its own runnable code cell
- Provide starter code: input data, variable name, structure
- Use `...` as the placeholder where the student fills in the solution
- Always end with a `print()` so output is immediately visible
- Include a `# hint:` comment for harder exercises
- Difficulty ramp: easy → medium → hard
  (mark harder ones with `*(Trudniejsze)*`)

### 5. Order all cells consistently
```
Title
Rozkład jazdy
---
## N. 🔹 Section name       ← numbered, emoji
Theory cells
Example cells
---
### ✏️ Ćwiczenia — topic  ← visual separator
Exercise descriptions (one markdown cell)
Exercise code templates  (one cell per exercise)
```

### 6. Add an agenda at the top
- Placed right after the title cell
- One line per section with emoji and short description
- Mark exercise sections with ✏️
- Keep it scannable — no more than 2 sub-items per section

### 7. Make it aesthetic
- Single `#` title header (not two separate lines)
- Numbered sections: `## 1.`, `## 2.`, …
- One emoji per section header (not per bullet point)
- Merge thin one-liner cells into their neighbours
- Remove redundant cells (e.g. duplicate headers after separators)
- Use comparison tables (`| | Imperative | Functional |`) to contrast concepts

### 8. Fill content gaps — for every concept taught, check for:
| Missing piece | Fix |
|---|---|
| Concept used before it's taught | Add theory + example before exercise |
| Step-by-step visualization needed | Add `traced_` fn that prints each step |
| "When to use X vs Y" decision guide | Add a comparison table + demo code |
| Surprising beginner behaviour | Add `⚠️` callout with runnable example |
| Built-in used but not explained (`zip`, `sorted` key…) | Add a subsection |

### 9. Exercise quality checklist
- [ ] No exercise uses a concept taught in a later section (BASIC_CONCEPTS.md are known)
- [ ] Each section has at least 3 exercises (easy / medium / hard)
- [ ] Nested or advanced syntax is explained before it appears in an exercise
- [ ] Templates are consistent: `...` for expressions, named variables for data
- [ ] Dict comprehension exercise: use `.items()` explicitly in the template

### 10. Version & metadata
- Update version number in the title cell after each significant revision
- Keep author name in the title cell
- update version into 2.0

### 11. Language & typography
- Use `-` (hyphen) instead of `—` (em dash) everywhere
- Write theory cells in Polish
- Technical/special names: write the Polish term first, then
  the English original in brackets — e.g. `klasa (class)`,
  `metoda (method)`, `dziedziczenie (inheritance)`
- text should be maximum 79 chars long
- Use academic/professional "we" voice (1st person plural) —
  `wywołujemy` not `wywołujesz`, `definiujemy` not `definiujesz`,
  `możemy` not `możesz`, `tworzymy` not `tworzysz`
