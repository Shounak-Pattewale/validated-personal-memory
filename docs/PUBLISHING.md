# Maintaining the public release

Repository: https://github.com/Shounak-Pattewale/validated-personal-memory

The repository is public. This update adds the live repository link to the manuscript and citation metadata, and reports the existing paired benchmark confidence intervals.

Copy the updated package files into your existing local clone, review the changes, then run:

```bash
git status
git add paper CITATION.cff CHANGELOG.md docs MANIFEST.json
git commit -m "Finalize paper availability and benchmark uncertainty reporting"
git push origin main
```

The package contains no `.git` directory. Preserve your existing clone's Git history. No arXiv ID, DOI or peer-review acceptance is claimed.
