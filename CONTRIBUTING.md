# Contributing Conventions

These conventions keep the repository history clear and make each team
member's contribution easy to verify during evaluation.

## 1. Start from an issue

Create or select an issue before beginning work. The issue should describe the
problem, expected files, and completion criteria.

Keep one main objective per issue. If the work grows into an unrelated task,
create a separate issue.

## 2. Branch naming

Use this format:

```text
name/issue-issuenumber-short-title
```

Rules:

- Use the contributor's first name in lowercase.
- Include the GitHub issue number.
- Use lowercase words separated by hyphens.
- Keep the short title specific and concise.

Examples:

```text
vivekananda/issue-12-repo-structure
manasa/issue-13-data-pipeline
shanker/issue-14-danet-training
```

Do not make unrelated changes on the same branch.

## 3. Commit messages

Commit messages must describe the actual change clearly.

Use an imperative action followed by the affected feature or artifact:

```text
Document DANet base-paper revision
Add reproducible malaria dataset split
Implement DANet-S attention blocks
Add baseline evaluation metrics
```

Avoid vague messages such as:

```text
update
changes
final
fix stuff
new code
```

Commit guidelines:

- Keep each commit focused on one logical change.
- Do not mix formatting, model changes, and result updates unnecessarily.
- Do not claim a result that has not been produced.
- Do not commit generated caches, credentials, datasets, or temporary files.

## 4. Pull requests

Each pull request should:

- Link the relevant issue.
- Explain what changed and why.
- List the files added or modified.
- State how the work was checked.
- Identify any unresolved limitation or follow-up task.
- Request review from another team member.

The reviewer should check technical correctness, notebook flow, file naming,
documentation, and whether the requested issue is fully addressed.

## 5. Notebook conventions

- Maintain one integrated Milestone 2 notebook.
- Add sections sequentially to avoid notebook merge conflicts.
- Keep Markdown explanations concise and evaluator-focused.
- Ensure execution order is sequential before final review.
- Remove failed experiments, temporary cells, and unrelated outputs.
- Keep figures close to the code and results they explain.
- Record seeds, package versions, training settings, and artifact locations.

Only one member should edit the integrated notebook at a time. Later members
should begin after the previous notebook work has been reviewed and integrated.

## 6. Files and artifacts

Do not commit:

- The NIH/NLM image dataset
- Dataset archives
- Credentials or tokens
- Environment files containing secrets
- Python cache directories
- Large model checkpoints

Small reproducibility artifacts, configuration files, split manifests,
training histories, plots, and evaluation tables may be included.

If a required checkpoint is too large, store it externally and document its
location, filename, file size, and checksum.

## 7. Contribution record

Update `CONTRIBUTIONS.md` after work has been reviewed. Record completed work,
not planned work. Include issue and pull-request references when available.
