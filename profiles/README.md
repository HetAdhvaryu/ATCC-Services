# Font Profiles

This directory contains **font profiles** used by the Legacy Font Converter engine.

A font profile is a **data-only definition** that describes how characters encoded
in a specific font should be interpreted and converted.

No executable logic lives here.

---

## 📌 Core Principles

- **No fonts are distributed** in this repository
- Profiles contain **only mapping data and metadata**
- All mappings must be **original and independently derived**
- Profiles must be **script-aware**
- Rule execution order is **strict and non-negotiable**

---

## 📁 Directory Structure

profiles/
│
├── gujarati/
│ ├── bhasha_bharti.json
│ ├── terafont_varun.json
│ ├── unicode.json
│ └── rules.json
│
└── README.md


Each script has its own directory.

---

## 🧠 What Is a Font Profile?

A font profile defines:
- Font metadata
- Script identity
- Encoding type (legacy or Unicode)
- Mapping table
- Applicable rule sets

Profiles are consumed by the core engine at runtime.

---

## 🧩 Font Profile Fields (Summary)

| Field | Description |
|------|-------------|
| `id` | Unique identifier for the profile |
| `font.name` | Display name of the font |
| `font.type` | `legacy` or `unicode` |
| `script.iso` | ISO 639-1 code (e.g. `gu`) |
| `encoding.base` | `ascii` or `unicode` |
| `rules` | Ordered rule IDs |
| `mapping` | Character/token mapping table |

---

## ⚙️ Rules vs Mapping (Very Important)

### Rules
- Handle **structural behavior**
- Examples:
  - Reph (ર્)
  - Pre-base matra (િ)
  - Conjunct normalization
- Defined once per script
- Reused across fonts

### Mapping
- Handles **glyph-to-glyph translation**
- Font-specific
- Must NOT contain logic

---

## 🛠️ How to Add a New Font (Step-by-Step)

### 1️⃣ Identify the Script
Create or reuse a script folder:
profiles/<script_name>/

Example:
profiles/gujarati/


---

### 2️⃣ Create Font Profile JSON
Create a new file:
<font_name>.json
Example:
terafont_varun.json


Follow the font profile schema strictly.

---

### 3️⃣ Define Mapping Table (Safely)

✔ Create mappings by:
- Typing known syllables in the source font
- Observing raw character output
- Mapping to known script tokens or target encoding

❌ Do NOT:
- Copy mappings from paid or cracked tools
- Reverse-engineer proprietary software
- Bundle font files

---

### 4️⃣ Assign Rule Sets
Reference existing rule IDs from `rules.json`.

Example:
```json
"rules": [
  "gu_reph",
  "gu_prebase_matra",
  "gu_conjuncts"
]
```

### 5️⃣ Validate the Profile

Before committing:
- Profile loads without errors
- Rule IDs exist
- Mapping table contains no duplicates
- Script ISO matches directory name

## 🧪 Testing Requirements

Every new font profile MUST include:
- Sample input text
- Expected output text
- Coverage for:
  - Matras
  - Reph
  - Conjuncts

Add tests under:
tests/samples/

## ⚠️ Legal & Ethical Requirements

- Do NOT distribute font binaries
- Do NOT copy mappings from proprietary tools
- Do NOT accept community contributions without review
- Profiles violating these rules will be removed

## 🧭 Best Practices

- Keep mappings minimal and explicit
- Prefer Unicode as an intermediate format
- Version profiles when changing mappings
- Document known limitations in font.notes

## 📦 Versioning Strategy

If mappings change:
- Increment profile version in id
- Keep old profile for backward compatibility

Example:
gu_bhasha_bharti_v2

## 📞 Support & Contributions

This project prioritizes accuracy over speed.
If you are unsure about a mapping:
- Open an issue
- Attach sample text
- Do NOT guess

## ✅ Final Reminder

A font profile is data, not code.
Treat it with the same care you would treat legal documents.
