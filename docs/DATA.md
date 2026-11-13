# Data and reproducibility scope

## Two distinct evaluations

The authored middleware comparison contains 60 shared queries, nine methods
and three models, yielding 1,620 answers. The public export includes aggregated
scores, family-level results, 486 state audit rows, 1,620 request-envelope checks,
and failed-answer records. It does not include every successful raw response,
all prompt payloads, or the complete middleware implementation.

The model-only benchmarks contain 41,486 cases per model: 39,000 adapted RULER,
500 LongMemEval-S and 1,986 LoCoMo-QA. `data/benchmarks/scores.csv.gz` contains
82,972 rows with model, suite, case ID, category, nominal length, status, prompt
hash, token/timing metadata, and saved score. These scores incorporate the saved
LongMemEval judge outcomes. Full judge response text is not included.

Question text, reference-answer text, benchmark histories and generated answer
text from the public benchmarks are excluded from this public release. The
original benchmark data remains governed by its upstream license. This release
can recalculate means, paired differences, clustered confidence intervals and
truncation sensitivities from scores, but cannot independently regrade answers.

## Files and provenance

`data/audit/` preserves every nonempty CSV/JSON evidence export from the paper
package, with private filesystem prefixes replaced by `archive://` logical
identifiers. Local temporary paths are replaced with deterministic pseudonymous
identifiers. These identifiers are not downloadable URLs. Original source hashes
identify archived inputs that are not necessarily distributed here.

`data/benchmarks/` also includes archived subgroup and sensitivity summaries.
Archived outputs are labelled as such in the notebook. They must not be mistaken
for analyses independently recomputed from answer text by this public package.
The manuscript reports the saved paired confidence intervals, which the public
analysis script reproduces from the released scores. Their interpretation remains
conditional on saved generations and the specified grouping assumptions.

`MANIFEST.json` hashes the actual distributed files after sanitisation. It is
separate from the original audit source manifests. No scores or numeric findings
were changed during path sanitisation.

## Interpretation

RULER uses an adapted scoring protocol. The three benchmark scales differ.
LongMemEval uses one automated judge, not human adjudication. Reasoning settings
and truncation counts differ by model. Bootstrap intervals are conditional on
saved generations and the specified grouping; they do not capture provider drift
or uncertainty in ground truth. Authored families are not independent natural
conversation samples. Exact stored states do not establish formal verification.
The failed acceptance gate remains a failure (119/120 supported cases).
