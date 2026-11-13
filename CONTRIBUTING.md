# Contributing

Report discrepancies with the file, row identifier, expected value and observed
value. Keep the authored middleware experiment separate from public benchmarks.
Do not overwrite historical scores to improve results. Add new analyses with
explicit assumptions and preserve the original metrics.

Run `python scripts/verify_results.py` and `python scripts/analyze_benchmarks.py`
before proposing analysis changes. Keep code offline and do not add API calls,
credentials, private paths or copyrighted benchmark text. Numerical corrections
must be documented in CHANGELOG.md. Contributions retain the applicable code
or content license.
