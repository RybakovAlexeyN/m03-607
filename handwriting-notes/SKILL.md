---
name: handwriting-notes
description: Convert typed notes and consented handwriting-reference photos into photographed A4 handwritten pages, with lossless pagination and mandatory content review.
compatibility: Image generation with reference images; optional Python 3.9+.
metadata:
  version: "0.1.0"
  language: "ru"
---

# Handwriting Notes

Use when a student supplies text and photos of their own handwriting and wants handwritten-looking A4 study notes.

## Inputs
- Original typed text (.txt/.md or pasted), preserved verbatim.
- 3–7 photos of the writer's own handwriting (or samples used with the writer's explicit permission).
- Optional layout: `two_columns` or `single_column`; mode: `precision` (default) or `visual`.

## Workflow
1. Freeze the text as the source of truth. Run `python3 handwriting-notes/scripts/pagepack.py prepare notes.txt --out work --mode precision` if Python is available.
2. Study the reference images: slant, Cyrillic letterforms, joins, stroke pressure, spacing, underlines, page geometry and paper texture. Never store private classmates' photos in public repositories.
3. Generate **one page at a time**, supplying the image generator with the references and the **exact page text** from `work/prompts/page-XX-precision.md`. No invented titles, sentences or marginal notes.
4. Review each image for the first and last lines, Cyrillic, numbers, abbreviations, all lines, missing content and repeats. Regenerate an invalid page with a smaller text chunk. Run `pagepack.py verify work --images work/renders` for presence/duplicate checks; this does not verify written text.
5. For exact checking, transcribe each generated image to `work/transcriptions/page-XX.txt` and run `pagepack.py verify work --transcriptions work/transcriptions`; do not assert 100% accuracy without thorough manual reading.
6. Deliver ordered page images with a clear report of which lines remain uncertain.

## Modes
**precision:** shorter pages, clear letters, readable layout; accuracy is the priority but not guaranteed by image models.
**visual:** close resemblance to organic handwriting and photographed paper, with the same required human content review.

Read `references/IMAGE_PROMPTS.md`, `references/STYLE_PROFILE.md`, `references/EVALS.md`, `references/USAGE_RU.md`.

## Important
Generative image models frequently introduce Cyrillic errors or duplicate pages. This skill handles **preparation, prompting and audit**, not direct image API calls or automatic faithful pen-stroke synthesis. Do not misrepresent generated notes as evidence they were physically handwritten.