# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About This Repository

A Polish-language Azure Cloud course for experienced QA Automation Engineers (Python/Pytest).
Content is delivered via Jupyter notebooks, with supporting Python scripts.
Part of the larger `KamilBartocha/courses` repo.

Target audience: Lead/Senior QA Automation Engineer, 5+ years Python experience,
working with Azure-based, API-driven, and Big Data systems.

## Running Code

```bash
# Open a notebook
jupyter notebook 01_azure_podstawy/01_azure_podstawy.ipynb

# Run a Python script directly
python3 02_azure_devops/02_cheat_sheet.py
```

## Module Structure

Twelve modules (01-12), each containing:
- `NN_cheat_sheet.py` - quick-reference code snippets
- `NN_exercise.py` - exercise starter code or solutions
- `NN_live_coding.py` - blank file used during live class sessions
- `NN_*.ipynb` - main Jupyter notebook with theory, examples, and exercises

Module topics:
01 Azure Podstawy -> 02 Azure DevOps CI/CD ->
03 AAD/Key Vault -> 04 Azure Storage ->
05 API Management -> 06 Service Bus/Event Hubs ->
07 Azure Functions -> 08 AKS/Containers ->
09 Monitor/App Insights -> 10 Big Data (ADF/Synapse) ->
11 Python SDK Patterns -> 12 Terraform IaC

Supporting reference: `syllabus-azure-basics.md` (Polish-language concept summary per module).

## Notebook Conventions (from `notebook-rules.md`)

When editing or refactoring notebooks, follow these rules:

**Language & naming**
- Theory/prose cells: Polish, academic "we" voice (`wywolujemy`, `definiujemy`, not `wywolujesz`)
- Code: English variable/function names (`blob_client`, `queue_name` - not `klient_blob`)
- Technical terms: Polish first, English in brackets - e.g. `kolejka (queue)`, `wyzwalacz (trigger)`
- Text line length: max 79 characters
- Use `-` (hyphen), not `---` (em dash)

**Cell structure per section**
```
## N. Section name
Theory cells (Polish prose)
Example cells (runnable English code)
---
### Cwiczenia - topic
Exercise descriptions (one markdown cell)
One code cell per exercise
```

**Exercise templates**
- Use `...` as the placeholder for student solutions
- Always end with `print()` so output is visible
- Add `# hint:` comments for harder exercises
- Difficulty ramp: easy -> medium -> hard (mark hard with `*(Trudniejsze)*`)
- Minimum 3 exercises per section

**Notebook metadata**
- Title cell: single `#` header with version (`1.0`) and author name
- Add agenda (Rozklad jazdy) cell after the title - one line per section with emoji
- Version number: update after significant revisions
