# Evaluation protocol — v0.1

Assess the output on independent axes:
1. **Lossless pagination:** reconstruct all source characters from page files; exact match.
2. **Readability:** owner can read pages at ordinary print scale.
3. **Text accuracy:** manually transcribe rendered pages and compare with frozen text (edit distance / character error rate). An OCR pass is not conclusive for cursive.
4. **Style resemblance:** writer rates visual similarity 1–5 without being told which samples were generated.
5. **Duplicates:** compare image similarity and unique first/last line; never assume different file names mean different pages.
6. **Completeness:** all pages supplied, none skipped, no hallucinated additions.

Test three distinct consenting writers, different writing styles and both visual/precision modes. Record failures and number of regeneration attempts. An accuracy claim must cite the actual measured test results; do not announce zero errors after only image generation.