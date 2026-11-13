# Publish this repository

Suggested name: `validated-personal-memory`

Suggested description: `Offline research artifacts for evaluating personal memory in language models: state correctness, answer reliability, token cost, and three public benchmarks.`

1. Extract the ZIP and open the `validated-personal-memory` directory.
2. Create an empty public GitHub repository with the suggested name. Do not
   initialise another README, license or gitignore, because these are included.
3. Run the commands below, replacing YOUR_REPOSITORY_URL with its actual URL:

```bash
git init
git add .
git commit -m "Release offline personal-memory research artifacts"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Use Git rather than the web uploader so hidden files such as `.gitignore` and
`.github/workflows/offline-checks.yml` are included. The ZIP contains no `.git`
directory. No repository has been created or published by preparing this package.

After publication, add the real repository URL to CITATION.cff and the paper's
availability statement. No arXiv ID, DOI or peer-review acceptance is claimed.
The included manuscript is the current draft; its release-pending availability
statement is intentionally unchanged until a repository exists.
