# qgis-plugin-copier-template

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
[![prek](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)

This template provides a starting point for QGIS plugin development, including
a working example plugin that can be used as a base when building your own functionality.

The generated project comes preconfigured with modern Python development tools
and best practices:

* **uv** for dependency management
* **Ruff** for code formatting and linting
* **ty** or **mypy** for static type checking
* **Flake8** for additional code quality validation (QGIS-specific checks and spellcheck)
* **Bandit** for security checks
* **Pytest** setup for automated testing
* **prek** hooks for running quality checks before commits
* **qgis-plugin-dev-tools** for developing and packaging QGIS plugins
* **qgis_plugin_tools** as a common QGIS plugin runtime library
* Optional **GitHub Actions** workflows for tests, code style checks and releases
* A **VS Code** workspace with recommended settings and extensions

## Requirements

* [QGIS](https://qgis.org/) >= 3.40 (QGIS 4 is also supported) with Python >= 3.12
* [Git](https://git-scm.com/)
* [uv](https://docs.astral.sh/uv/)

## Creating a new QGIS plugin project from the template

Create a new folder and initialize it as a Git repository:

```bash
mkdir my-qgis-plugin
cd my-qgis-plugin
git init
```

### Setting up a virtual environment

<details><summary>Set up a virtual environment</summary>

The template is applied and the plugin is developed in a Python virtual
environment that has access to the libraries provided by the QGIS installation.

Install [uv](https://docs.astral.sh/uv/) if not already available

On Linux:

* Create a Python virtual environment with access to the libraries provided by
  the QGIS installation:

  ```bash
  uv venv .venv --system-site-packages
  # to ensure correct python is used you can set env variable:
  # UV_PYTHON=/usr/bin/python3 uv venv .venv --system-site-packages
  ```

On Windows:

* You can use the [qgis-venv-creator tool](https://github.com/GispoCoding/qgis-venv-creator)
  to make sure the virtual environment is configured correctly for QGIS

> [!NOTE]
> if it is not possible to install uv globally, install it to virtual env
>
> ```bash
> python -m pip install --upgrade pip
> pip install uv
>  ```

</details>

### Running Copier

After setting up a virtual environment in the folder,
activate it and run Copier with `uvx` (check the supported version in
[copier.yml](copier.yml)):

```bash
uvx copier copy --answers-file .copier-answers.qgis-plugin.yml https://github.com/osgeosuomi/qgis-plugin-copier-template.git .
```

Copier prompts for the template questions and uses the
answers to populate the template. Then
[finish the setup](#after-applying-the-template).

## Applying the template to an existing project

If the repository does not have a virtual environment yet,
[set one up](#setting-up-a-virtual-environment). Activate it and apply the
template with the same command as for a new project:

```bash
uvx copier copy --answers-file .copier-answers.qgis-plugin.yml https://github.com/osgeosuomi/qgis-plugin-copier-template.git .
```

Use the `--answers-file` option and name the configuration file
`.copier-answers.qgis-plugin.yml` so that other Copier templates
(for example CI) can also be used in the same repository.

After answering the prompts, Copier will ask whether it can overwrite existing
files (if any found). Answer **yes** to all prompts, then review the Git diff
and check that repository-specific customizations are not removed. Then
[finish the setup](#after-applying-the-template).

## After applying the template

Generate the lock file, install the project dependencies and the Git hooks:

```bash
uv lock --upgrade
uv sync
uv run prek install
```

See the `DEVELOPMENT.md` file in the target repository for instructions on
setting up your QGIS plugin development environment.

If you want to modify your answers, rerun Copier with:

```bash
uvx copier recopy --answers-file .copier-answers.qgis-plugin.yml .
```

## Updating from the template

When the template is updated, apply changes to the target repository and sync
the environment with the updated dependencies:

```bash
copier update --answers-file .copier-answers.qgis-plugin.yml --skip-answered
uv lock --upgrade
uv sync
```

## Using the template for a plugin component of a monorepo

Answer **yes** to `is_monorepo_component` when the plugin is one component (uv
workspace member) of a larger repository, and run Copier with the component
directory as the destination:

```bash
uvx copier copy --answers-file .copier-answers.qgis-plugin.yml \
  https://github.com/osgeosuomi/qgis-plugin-copier-template.git components/plugin
```

Only the plugin component is generated, never files owned by the wider project
(`.editorconfig`, `.gitlint`, VS Code workspace, GitHub workflows). The
component is self-contained and only needs to be listed in
`[tool.uv.workspace] members` of the root `pyproject.toml`.

The component's `.pre-commit-config.yaml` is discovered by prek as a
[nested project](https://prek.j178.dev/reference/workspace/). It is generated
as `orphan`, so the root hooks do not run on the component and the root
configuration does not need to know about it. Configuration shared with the
root, such as `[tool.ruff] extend` or `changelog_file_path`, is edited into the
generated files and kept by updates.

The answers file is stored in the component directory, so updates are run there
too:

```bash
cd components/plugin
copier update --answers-file .copier-answers.qgis-plugin.yml --skip-answered
```

## Template development

See [development readme](./docs/DEVELOPMENT.md).

## Contributing

Contributions are very welcome. Get started by reading OSGeo
Suomi [CONTRIBUTING guidelines](https://github.com/osgeosuomi/.github/blob/main/CONTRIBUTING.md).

## License

qgis-plugin-copier-template is licensed under the GNU General Public License,
version 2 or (at your option) any later version (`GPL-2.0-or-later`).
See [LICENSE](LICENSE) for the full text of GPLv2. Every source file carries
a license notice.

By contributing to this project you agree that your contributions are
licensed under the same terms.
