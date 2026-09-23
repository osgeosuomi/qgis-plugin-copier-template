# Template development

Create a python virtual environment and install `prek`:

```bash
pip install prek
prek install
```

## Making changes to the template

Depending on the type of change, you can either modify the template directly
or implement and test the change first in a repository that already uses the template.

If another plugin repository is used for testing:

1. Make the required changes in the repository that already uses the
template and verify that they work as expected.

2. Apply the same changes to the template repository in a feature branch.

3. Stash the changes from step 1 and update the plugin repository from your
template feature branch by using `--vcs-ref=<branch>` with Copier `update` command

    ```bash
    copier update --answers-file .copier-answers.qgis-plugin.yml --vcs-ref=<branch>
    ```

4. If the update does not work as expected, repeat steps 2 and 3.

5. Merge the feature branch into `main`. The automatic release process
starts after the merge.

## Automatic Releases

This repository uses [Conventional Commits] and [python-semantic-release].

> [!NOTE]
> Only use `feat` and `fix` for changes that affect the files in the `template` folder
> and should therefore trigger a new release. Use other types (`chore`, `ci`, `docs`
> etc) for other commits in this repository.

When changes are pushed to `main`, python-semantic-release checks the commits
since the previous release. If one or more `feat` or `fix` commits are found, a
new release is created automatically. The next version number and release notes
are generated from the commit history.

Use the following scopes with `feat` and `fix` commits:

- `ci` - GitHub workflows, CI/CD
- `lint` - linters, formatters, pre-commit hooks and code quality checks
- `plugin` - changes to generated QGIS plugin files in `src` (and `test`) folder
- `deps` - dependency additions, removals, and updates
- `chore` - miscellaneous project maintenance tasks that do not fit another scope
- Additional scopes may be used where appropriate, to better describe the change

Examples:

```text
feat(ci): add release workflow
fix(plugin): correct generated metadata
feat(lint): add markdownlint
fix(deps): pin incompatible dependency
```

[Conventional Commits]: https://www.conventionalcommits.org/en/v1.0.0/
[python-semantic-release]: https://python-semantic-release.readthedocs.io/en/latest
