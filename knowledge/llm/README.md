# LLM Corpus

[`llm-corpus.md`](llm-corpus.md) is the deterministic full-context projection of the canonical Encyclopedia Markdown. It is generated only from the shared semantic IR. Each document declares its stable ID, source path, area, and namespace context; each retained section declares its stable ID and preserves structured prose, tables, lists, code, links, and explicit cue summaries for applicability, cautions, uncertainty, and provenance.

The corpus excludes `guides/`. Its source text has already passed the mandatory privacy source gate. Run `python build.py` to regenerate it and `python check.py` to validate freshness, bytes, and privacy.
