#!/usr/bin/env python
# Copies the monorepo root fixture to the given directory, rendering the .jinja files
# so that the lint rules come from includes/plugin_lint.jinja. Dotfiles are stored
# undotted, so that the tooling of this repository does not pick them up.
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

FIXTURE = Path(__file__).parent / "monorepo-root"
TEMPLATE_ROOT = Path(__file__).parents[1]
DOTTED = {
    "env.example": ".env.example",
    "gitignore": ".gitignore",
    "gitlint": ".gitlint",
    "markdownlint.jsonc": ".markdownlint.jsonc",
    "pre-commit-config.yaml": ".pre-commit-config.yaml",
}
# Matches how the test builds generate the plugin
ANSWERS = {"insert_copyright_header": False, "qgis_version": "QGIS3"}


def main(target: Path) -> None:
    environment = Environment(
        loader=FileSystemLoader(TEMPLATE_ROOT), keep_trailing_newline=True
    )
    target.mkdir(parents=True, exist_ok=True)
    for source in sorted(FIXTURE.iterdir()):
        name = source.name.removesuffix(".jinja")
        destination = target / DOTTED.get(name, name)
        if source.name.endswith(".jinja"):
            template = environment.get_template(
                source.relative_to(TEMPLATE_ROOT).as_posix()
            )
            destination.write_text(template.render(**ANSWERS))
        else:
            destination.write_text(source.read_text())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: create-monorepo-root.py TARGET_DIR")
    main(Path(sys.argv[1]))
