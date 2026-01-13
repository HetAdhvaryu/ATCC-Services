## Product Name
Legacy Font Converter

## Problem Statement
Millions of legal and administrative documents in India are still typed using
legacy (non-Unicode) fonts. Re-typing or retraining operators is costly, slow,
and error-prone.

Existing converters are expensive, closed, and inflexible.

## Goals
- Allow users to continue typing in their familiar legacy fonts
- Convert documents accurately into required target fonts
- Support legal-grade document accuracy
- Enable both offline desktop usage and online service model

## Target Users
- Court DTP shops
- Typing bureaus
- Legal documentation vendors
- Digitization agencies
- Small publishers

## In-Scope (Phase 1)
- Gujarati script support
- Bhasha Bharti → Terafont Varun conversion
- Desktop application (offline)
- Text-based conversion (copy-paste)

## Out of Scope (Phase 1)
- OCR
- PDF layout preservation
- Font distribution
- Cloud-only dependency

## Functional Requirements
1. Convert text deterministically (same input → same output)
2. Preserve matras, reph, conjuncts
3. Handle documents up to 100 pages
4. Simple UI usable by non-technical users

## Non-Functional Requirements
- Offline operation
- Cross-platform compatibility
- No internet requirement
- Fast conversion (<1 sec per page)
- High reliability

## Success Metrics
- Zero character loss
- Legal document acceptance
- <1% manual correction required

## Risks
- Incorrect rule ordering
- Incomplete mapping tables
- User selecting wrong source font

## Mitigations
- Script-aware rule engine
- Extensive test corpus
- Clear UI font selection
