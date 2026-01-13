# Legacy Font Converter

A cross-platform, offline-first engine for converting Indian legacy (non-Unicode)
fonts into other legacy fonts or Unicode, with legal-document accuracy.

---

## 🎯 Why This Exists

Millions of legal, court, and administrative documents in India are still typed
using legacy fonts due to years of operator muscle memory. However, modern workflows
often mandate specific fonts or Unicode compliance.

Re-typing or retraining is costly, slow, and error-prone.

This project allows users to **continue typing in familiar fonts** while producing
**compliant output fonts**.

---

## ✨ Key Features

- Legacy → Legacy font conversion
- Legacy → Unicode → Legacy safe pipeline
- Script-aware rule engine
- Offline desktop application
- Cross-platform (Windows, Linux, macOS)
- Designed for legal and government documents
- Extensible font profile system

---

## 🧠 Supported Scripts (Initial)

- Gujarati
  - Bhasha Bharti
  - Terafont Varun
  - Unicode Gujarati

---

## 🖥 Platforms

- Windows (primary)
- Linux
- macOS

---

## 🚀 Quick Start (Development)

```bash
git clone https://github.com/your-org/legacy-font-converter.git
cd legacy-font-converter
python desktop/app.py

