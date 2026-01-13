# Architecture Overview

## High-Level Design
The system is built around a font-agnostic conversion engine driven by
data-defined rules and mappings.

Input Text
↓
Rule Engine (script-specific)
↓
Character Mapping
↓
Output Text

## Core Principles
- Data-driven (rules & mappings in JSON)
- Deterministic processing
- Script-aware, font-agnostic core
- UI and API as thin layers

## Modules

### core/engine.py
Orchestrates the conversion pipeline:
1. Rule application (ordered)
2. Character mapping
3. Output generation

### core/rule_engine.py
Executes transformation rules defined in JSON:
- Regex-based
- Ordered execution
- Script-specific

### profiles/
Contains font definitions:
- Mapping tables
- Applicable rules
- Script metadata

No code changes required to add a new font.

### desktop/
Thin UI layer using Tkinter:
- Input text
- Source font selection
- Target font selection
- Output text

### api/ (future)
FastAPI-based service:
- File upload
- Batch conversion
- Metered usage

## Rule Execution Order (Gujarati)
1. Reph handling (ર્)
2. Pre-base matra (િ)
3. Conjunct normalization
4. Vowel signs
5. Base consonants

Order is strictly enforced.

## Extensibility
- New font: add JSON profile
- New script: add rules + profiles
- New UI: reuse core engine

## Packaging
- PyInstaller for Windows desktop
- Docker for API service

## Security & Legal
- No proprietary font redistribution
- Original mapping tables only
- User-installed fonts
