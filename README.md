# Handwriting Notes

A reusable AI-agent skill for converting typed lecture notes into photographed-looking A4 handwritten pages, guided by **samples of the writer's own handwriting**.

> **Status: v0.1 prototype.** The Python utility prepares lossless page chunks, prompts and checks. It does **not** generate images by itself. An image generation tool that accepts references is required, and generated Cyrillic must be visually checked. Never treat a realistic-looking photo as proof of exact wording.

## Для одногруппников

1. Подготовьте исходный текст в UTF-8 (`.txt` / `.md`).
2. Добавьте 3–7 фотографий **собственного** почерка или образцов, использование которых разрешил автор.
3. Передайте агенту папку `handwriting-notes/` как skill и попросите: «Используй handwriting-notes, сделай страницы А4 в режиме precision, сохрани все слова и проверь каждую страницу».
4. Агент создаёт отдельные страницы по очереди с помощью доступного генератора изображений. **Вручную проверьте каждую страницу** на ошибки, пропуски и повторения.

Подробная инструкция: [handwriting-notes/references/USAGE_RU.md](handwriting-notes/references/USAGE_RU.md).

## Prepare pages locally

Requires Python 3.9+ (standard library only).

```bash
python3 handwriting-notes/scripts/pagepack.py prepare notes.txt --out work --mode precision --layout two_columns --max-chars 1300
```

Creates `work/original.txt`, `work/pages/page-XX.txt`, `work/prompts/page-XX-precision.md` and `work/manifest.json`.

After generating your pictures, save them as `work/renders/page-01.png`, etc.:

```bash
python3 handwriting-notes/scripts/pagepack.py verify work --images work/renders
```

This checks page integrity and looks for duplicate/missing image files. It **cannot confirm the lettering inside the pictures**. To compare exact transcriptions, place manually transcribed page text into `work/transcriptions/page-XX.txt` and run:

```bash
python3 handwriting-notes/scripts/pagepack.py verify work --transcriptions work/transcriptions
```

## Run tests

```bash
python3 -m unittest discover -s handwriting-notes/tests -v
```

## Contents

- [SKILL.md](handwriting-notes/SKILL.md) — agent workflow
- [IMAGE_PROMPTS.md](handwriting-notes/references/IMAGE_PROMPTS.md) — rendering instructions
- [STYLE_PROFILE.md](handwriting-notes/references/STYLE_PROFILE.md) — reference-photo analysis checklist
- [EVALS.md](handwriting-notes/references/EVALS.md) — evaluation protocol
- [USAGE_RU.md](handwriting-notes/references/USAGE_RU.md) — guide in Russian
- [pagepack.py](handwriting-notes/scripts/pagepack.py) — lossless pagination & audit CLI
- [test_pagepack.py](handwriting-notes/tests/test_pagepack.py) — unit tests

## Privacy and academic integrity

Do not commit classmates' handwriting photos or personal data to a public repository. Check your course's rules before submitting generated notes as handwritten work. The tool is for preparing notes, not proving they were physically handwritten.
