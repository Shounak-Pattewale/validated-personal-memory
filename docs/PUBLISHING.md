# Maintaining the public release

Repository: https://github.com/Shounak-Pattewale/validated-personal-memory

## Preprint

- Title: Validated Personal Memory for Language Models: A Bounded Study of State Correctness, Answer Reliability, and Processing Cost
- Author: Shounak Pattewale (https://orcid.org/0009-0003-4828-9333)
- Version: 1.0
- Publication date: 2026-11-14
- Zenodo record: https://zenodo.org/records/24210707
- Version DOI: https://doi.org/10.5281/zenodo.24210707

This is a research preprint. No arXiv identifier or peer-reviewed acceptance is claimed. The DOI identifies the paper, not a separately archived software release.

Copy the changed files into your existing clone, preserving directory paths, then review and commit:

```bash
python scripts/verify_manifest.py
git diff -- README.md CITATION.cff CHANGELOG.md docs/PUBLISHING.md MANIFEST.json
git add README.md CITATION.cff CHANGELOG.md docs/PUBLISHING.md MANIFEST.json
git commit -m "Add Zenodo preprint DOI and author ORCID"
git push origin main
```

Preserve your existing clone's Git history. For later releases, keep CITATION.cff, publication links and MANIFEST.json consistent with the files being distributed.
