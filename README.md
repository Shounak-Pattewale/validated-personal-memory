# Validated Personal Memory

Research artifacts for **Validated Personal Memory for Language Models: A Bounded
Study of State Correctness, Answer Reliability, and Processing Cost**, by
**Shounak Pattewale**.

[Read the paper](paper/paper.pdf) | [Offline notebook](notebooks/offline_analysis.ipynb) | [Data scope](docs/DATA.md)

This repository analyses saved experiments. **No model API keys, GPU, Drive mount,
or model API calls are required.** Installing Python packages requires an internet
connection once; the analysis itself runs offline.

## What this study examines

A memory system must preserve accepted facts, handle replacements and forgetting,
and return correct answers from its records. We measure state correctness,
answer accuracy and token use separately. A second evaluation measures two
models on three public benchmarks without the middleware.

### Authored middleware evaluation

Six task families, two background conditions, five queries per episode, nine
methods and three models produce 1,620 answer outputs over shared questions.

| Method | DeepSeek | Gemma | GLM |
| --- | ---: | ---: | ---: |
| Full history | 60/60 | 37/60 | 51/60 |
| Selected records | 60/60 | 60/60 | 57/60 |
| All visible records | 60/60 | 60/60 | 60/60 |

All 486 audited states match their references. Selected-record memory consumes
19.0% to 26.4% more total model tokens than full history when interpretation is
included. The earlier acceptance study retains one failed supported case.

### Model-only public benchmarks

| Benchmark | Cases per model | Gemma | Nemotron |
| --- | ---: | ---: | ---: |
| RULER, adapted | 39,000 | 0.970581 | 0.950550 |
| LongMemEval-S | 500 | 0.790000 | 0.586000 |
| LoCoMo-QA | 1,986 | 0.530313 | 0.425724 |

These are different metrics, not one common accuracy scale. The 82,972 saved
score rows are included. LongMemEval outcomes derive from 1,000 saved automated
judgments. These benchmark runs **do not evaluate the middleware**.

## Run offline analysis

Python 3.12 is the tested environment. From the repository root:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/verify_manifest.py
python scripts/verify_results.py
python scripts/analyze_benchmarks.py
python scripts/build_figures.py
```

The first two verification scripts use only the Python standard library.
The benchmark script recomputes means, paired differences and 20,000-sample
clustered bootstrap intervals from saved scores. It also calculates the effect
of excluding truncated answers and an extreme truncation sensitivity bound.
It does not generate, repair or independently regrade answers.

For the clean notebook, install `requirements-notebook.txt`, launch
`jupyter lab`, and open `notebooks/offline_analysis.ipynb`. Run all cells in order.
For Colab, upload and extract the complete repository first; keep the notebook
inside its `notebooks` directory or run from the extracted repository root.
No cell installs packages or makes network requests automatically.

## Repository contents

- `paper/`: current PDF, LaTeX source and original figures.
- `notebooks/`: clean offline analysis notebook.
- `scripts/`: numerical checks, paired benchmark analysis and figure generation.
- `data/audit/`: sanitised evidence tables and archived audit reports.
- `data/benchmarks/`: all public score rows and archived diagnostic summaries.
- `docs/`: data scope, provenance, third-party references and publishing steps.
- `results/`: location for locally regenerated outputs.

## Build the manuscript

A LaTeX installation with the packages listed in the source is required:

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The prebuilt PDF is included. No manuscript build is needed to run the analysis.

## What is and is not reproduced

Included files support aggregate middleware checks, state-audit inspection and
per-question public score analyses. Full benchmark question/reference/answer text,
raw provider request archives, and the complete middleware implementation are
not part of this release. Archived scorer audits are evidence from earlier runs;
this public package does not repeat those text-level audits. See [data scope](docs/DATA.md).

The authored workload is small and synthetic. Provider aliases and reasoning
settings vary. The summary metric penalises upstream failures. Correct state
alone does not prove correct interpretation, secure deletion or general memory
reliability. This is a manuscript draft and artifact release, not a claim of
peer-reviewed acceptance or a production-ready memory system.

## Citation and licenses

Use CITATION.cff for artifact attribution. No DOI or arXiv identifier has been
assigned in this package. Code is MIT licensed; original manuscript and analysis
content use CC BY 4.0. See LICENSE, LICENSE-CONTENT.md and docs/THIRD_PARTY.md.
