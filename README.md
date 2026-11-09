# Boolean Search Engine

A Python inverted index with Boolean search: whitespace means OR, `&` means AND, and AND has higher precedence. The program includes a small synthetic demonstration and can read user-supplied JSONL documents.

## Course and original date

- **Course / المادة:** CSC 484 - Information Retrieval / استرجاع المعلومات, King Saud University.
- **Original project period / تاريخ المشروع الأصلي:** Spring 2024; surviving notebook last saved 6 May 2024.
- **Evidence:** The project brief is named Spring 2024 and describes CSC484 Project 1. The original `Project_1_CSC484` notebook retains a 6 May 2024 modification date. This is a source-save date, not a verified submission date.

The original coursework dates above are distinct from the GitHub publication and maintenance date, **9 November 2026**. The original source files were preserved locally.

## Run

Python 3.9 or newer. Uses only the Python standard library.

```sh
python search_engine.py
```

## Verification

```sh
python -m unittest discover -s tests -v
```

12 unit tests and the synthetic CLI demonstration passed. Checks use newly authored synthetic inputs only. See [CHANGES.md](CHANGES.md) for the publication changes and validation scope.

## Scope and provenance

Uses whitespace tokenization and lowercase normalization only. There is no stemming, punctuation stripping, ranking, or phrase search. Original news data and experiment outputs are excluded.

Published from the owner's local coursework. Course briefs, slides, exams, student identifiers, faculty names, real datasets, collected email, credentials, IDE history, and compiled files are excluded. Academic material may include supplied interfaces or collaborative code; no claim of sole authorship of all scaffolding and no blanket license is made.

Course titles are cross-checked against the [KSU computer science course catalog](https://ccis.ksu.edu.sa/en/cs/cs-prog-guides). Original local evidence is retained privately rather than publishing the source briefs/reports.
