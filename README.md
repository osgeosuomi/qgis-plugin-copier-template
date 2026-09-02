# qgis-plugin-copier-template

This template provides a starting point for QGIS plugin development, including a working example plugin that can be used as a base when building your own functionality.

The generated project comes preconfigured with modern Python development tools and best practices:

* **uv** for dependency management
* **Ruff** for code formatting and linting
* **Mypy** for static type checking
* **Flake8** for additional code quality validation (including QGIS-specific checks)
* **Pytest** setup for automated testing
* **pre-commit** hooks for running quality checks before commits
* **qgis-plugin-dev-tools** for developing and packaging QGIS plugins

## Creating a new QGIS plugin project from the template

Create a new folder and initialize it as a Git repository:

```bash
mkdir my-qgis-plugin
cd my-qgis-plugin
git init
```

Next, create a Python virtual environment which will also be used later in QGIS plugin development.

On Linux:

* Install [uv](https://docs.astral.sh/uv/) if not already available: `pip install uv`
* Create a Python virtual environment with access to the libraries provided by
  the QGIS installation:
  `uv venv .venv --system-site-packages`

On Windows:

* You can use the [qgis-venv-creator tool](https://github.com/GispoCoding/qgis-venv-creator)
  to make sure the virtual environment is configured correctly for QGIS
* Install `uv` to the virtual environment: `pip install uv`

Once the virtual environment is ready, activate it, install Copier (check the supported version in [copier.yml](copier.yml)), and run the following command:

```bash
pip install copier
copier copy --answers-file .copier-answers.qgis-plugin.yml https://github.com/osgeosuomi/qgis-plugin-copier-template.git .
```

The Copier tool will prompt you for the required values and use them to populate the template. If you want to modify your answers, rerun Copier with:

```bash
copier recopy --answers-file .copier-answers.qgis-plugin.yml .
```

After the template has been applied to the target repository, generate the lock file and install the project dependencies::

```bash
uv lock
uv sync
```

Finally, see the `DEVELOPMENT.md` file in the target repository for instructions on setting up your QGIS plugin development environment.

## Applying the template to an existing project

Add Copier (check the supported version in [copier.yml](copier.yml)) as a development dependency in the repository.

Apply the template files with the `copier copy` command. On the first run, the tool will prompt for required values.

Use the `--answers-file` option and name the configuration file `.copier-answers.qgis-plugin.yml` so that other Copier templates (for example, CI) can also be used in the same repository.

```bash
copier copy --answers-file .copier-answers.qgis-plugin.yml https://github.com/osgeosuomi/qgis-plugin-copier-template.git .
```

After answering the prompts, Copier will ask whether it can overwrite existing files (if any found). Answer **yes** to all prompts, then review the Git diff and check that repository-specific customizations are not removed.

If you want to modify your answers, rerun Copier with:

```bash
copier recopy --answers-file .copier-answers.qgis-plugin.yml .
```

## Updating from the template

When the template is updated, apply changes to the target repository with:

```bash
copier update --answers-file .copier-answers.qgis-plugin.yml --skip-answered
```

## Template development

Create a python virtual environment and install `prek`:

```bash
pip install prek
prek install
```

### Updating the template

1. Make the required changes in a repository that already uses the template and verify that there are no syntax errors etc.

2. Apply the same changes to the template repository via a feature branch.

3. Stash the changes made in step 1 and update through the template. Using `--vcs-ref=<branch>` allows testing the against any changes without creating a tag.

    ```bash
    copier update --answers-file .copier-answers.qgis-plugin.yml --vcs-ref=<branch>
    ```

4. If the update does not work as expected, repeat steps 2 and 3.

5. Once the changes have been validated and merged to `main`, create a new tag in the template repository and document the changes in the tag message.

    ```bash
    git tag -a v0.1.0

    # Document the changes to tag message

    git push --tags
    ```

6. Run `copier update` once more in the target repository from step 1, this time **without** `--vcs-ref=HEAD`. This updates `.copier-answers.qgis-plugin.yml` to the latest tag. Squash or rebase the changes into a single commit, for example:

    ```bash
    git commit -m "chore: update from qgis-plugin-copier-template"
    ```
