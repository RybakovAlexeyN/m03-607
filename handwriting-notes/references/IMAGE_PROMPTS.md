# Image-generation prompt template

Attach several reference photographs from **the same consenting writer** and insert the exact contents of only **one** `pages/page-XX.txt` file.

Generate a single realistic overhead smartphone photo of a portrait A4 sheet on a neutral wooden desk. Write only the supplied PAGE_TEXT in the reference writer's ordinary Russian cursive. Respect their letter shapes, connections, ink color, line spacing, baseline variation, header underlines, margins and (if requested) an imperfect two-column separator. Use organic pen pressure and minimal paper folds; no aged-paper filter or ornate calligraphy. **No invented symbols or textual additions.** Keep all Cyrillic characters, numbers, headings, abbreviations, punctuation and arrows exactly as input.

Two-column option: first complete the left column, then continue in the right. Single-column option: use generous margins. For precision mode favor short text and clarity; for visual mode favor fidelity and organic page texture, never at the expense of source coverage.

## Page uniqueness
A `page-XX` request must contain **only** its respective PAGE_TEXT, not the prior page's content. Verify the first and last lines before accepting the output.

## Known limitations
An image that looks correct may have corrupt words. If errors persist, use smaller page portions or deterministic typesetting with a handwriting font owned by the user. Never promise perfect handwriting replication or character-for-character fidelity from an image model alone.