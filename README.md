# ATCC-Services
DTP Job services served using latest technology for accuracy, performance and reliability 

# Legacy Font Converter

A cross-platform, offline-first engine for converting Indian legacy (non-Unicode) fonts
used in DTP and legal documents into other legacy fonts or Unicode.

## 🎯 Purpose
Many Indian DTP professionals still type in legacy fonts (e.g., Bhasha Bharti, KrutiDev)
due to years of muscle memory. However, legal and government workflows increasingly
require specific fonts or Unicode.

This project solves that problem without forcing users to relearn typing.

## ✨ Features
- Legacy → Legacy font conversion
- Legacy → Unicode → Legacy safe pipeline
- Script-aware rule engine (Gujarati first)
- Offline desktop application
- Extensible font profile system
- Designed for legal-document accuracy

## 🧠 Supported Scripts
- Gujarati (initial)
  - Bhasha Bharti
  - Terafont Varun
  - Unicode

## 🖥️ Platforms
- Windows
- Linux
- macOS

## 🚀 Quick Start (Developer)
```bash
git clone https://github.com/your-org/legacy-font-converter.git
cd legacy-font-converter
python desktop/app.py
```

## Important Notes

This project does NOT distribute fonts.

Users must install required fonts separately.

Conversion accuracy depends on correct font selection.

## 📌 Roadmap

See docs/roadmap.md

## 📜 License

See LICENSE
