# CHANGELOG

<!-- version list -->

## v0.5.0 (2026-09-24)

### Bug Fixes

- **chore**: Remove invalid build key from the project table
  ([`e576449`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/e576449868a3add186f2e776797eeae9a30ae6c9))

- **lint**: Ignore CHANGELOG.md from markdownlint
  ([`85b4ca9`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/85b4ca94396bf6eff19439fcb47b0e92f560ad7c))

- **plugin**: Do not ask python version
  ([`2fb2bdc`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/2fb2bdc759dba7669a02076c13e9f4476b5a50ee))

- **plugin**: Make repository url required
  ([`04dcc30`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/04dcc30012877e37e365753b73dd9a2ff9bd4ef9))

### Documentation

- Add DEVELOPMENT.md
  ([`f490464`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/f49046456c69dea55c4b98a6ab54fa277e03878c))

- Fix typos in readme files
  ([`4db1a0e`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/4db1a0e4410d59d1cc855c49490e33f828136ac6))

### Features

- **chore**: Freeze prek hooks to newest versions
  ([`58f43da`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/58f43da669161a429f9495c0ee0879206be9e109))

- **chore**: Set debugpy as default debugger and update its version
  ([`27224ea`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/27224ea826f84be13438606350388e192d1c775f))

- **chore**: Set pytest test path in pyproject.toml
  ([`ac6a203`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/ac6a203e1daf400c302ccc9afd065e1bac24157e))

- **ci**: Lint commit messages in code style workflow
  ([`fa8dbdc`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/fa8dbdca3b2e14232afaf5b6fa4a9d15aaee16c5))

- **ci**: Make workflow names more descriptive
  ([`40d8ffc`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/40d8ffc8e610438cd84a57c2a304d463fa79ff8b))

- **ci**: Run lint and tests before release
  ([`cccca0d`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/cccca0d3ff07b7e734a4e8fb927cf850f6ad2d95))

- **lint**: Add qgis-stubs for QGIS3 plugins
  ([`0bf90dc`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/0bf90dccd29313ae4399757546258f32a6c42c13))

- **plugin**: Add a placeholder icon
  ([`86cd99e`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/86cd99e4ed2544f4ce713f8b52fa9e41b5fb76ff))

- **plugin**: Add question for metadata about text
  ([`a524dfe`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/a524dfe3e93286f518b332c20ae64335ebc009d5))

- **vscode**: Add QGIS debugpy launch configuration
  ([`5e895c1`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/5e895c1d734dd704c88c507d747a38a9b3d1ba85))


## v0.4.0 (2026-09-22)

### Features

- Add support for monorepo projects
  ([`4206663`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/4206663419b295e410da5e0fb369e47c91d60e75))

- **ci**: Check code coverage on pull requests
  ([`4777471`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/477747124ba2ddf03b8b0f1a06c56f649ada9abb))

- **ci**: Make code coverage check optional
  ([`f8ea899`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/f8ea899c947ef752cd9ffb1435728db4440a81e1))


## v0.3.1 (2026-09-20)

### Bug Fixes

- Install Qt translation tools if needed
  ([`37aebbd`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/37aebbd82402757d0a501a4de19606e999fa5fc2))


## v0.3.0 (2026-09-20)

### Features

- Add actionlint hook
  ([`346ac6d`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/346ac6d8d1a19951a786e353cab665d0e77851b5))

- Add initial GitHub workflows for the plugin
  ([`5e495a9`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/5e495a96a5aa2d82dc58a8a1095dc8091e05e943))


## v0.2.0 (2026-09-20)

### Bug Fixes

- Fix markdown and toml linter errors
  ([`be50524`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/be505242fdef9f5709b91b152ee3f58b5b893767))

- Move some imports to TYPE_CHECKING
  ([`00963c1`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/00963c183fddc1dbf09cd2779d9d76e14eb9bc05))

- Remove copyright headers from all files
  ([`30b3b9e`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/30b3b9e1de978ee69ba8965387c782fa7fa50551))

- Use newest qpdt that will update translations with QGIS4
  ([`39ef43b`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/39ef43b11930a999abaeb1ef16bd225bdc87ae31))

- **linting**: Select flake8-qgis rules based on target QGIS version
  ([`a749abf`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/a749abf764dca66ab1164cee33e29318fa0da381))

- **prek**: Use configured python version in pre-commit checks
  ([`a11c809`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/a11c8091c9e5b421927adacb1b58b664cfe92606))

### Features

- Add answer about qgis plugin class name
  ([`fa60164`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/fa60164b4ed68211dd01248259042b0c13a75e14))

- Add normalize-xml hook
  ([`d524359`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/d52435974a931b5584ca0d9f976963b93505d807))

- Use uv build backend instead of setuptools
  ([`65d964f`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/65d964fafdc210848a71449179e539ee2af172ca))

- **docs**: Update DEVELOPMENT.md
  ([`2f26a8e`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/2f26a8eadcbc65c8e78ada9fe9703e4a53052927))

- **linting**: Add pre-commit hook to check markdown and toml files
  ([`55ea2b3`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/55ea2b3a0ab9cdf2c3f9f591d9d3048f07edc03a))

- **vscode**: Add markdownlint to recommended extensions
  ([`7025e2d`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/7025e2ded2d7390842171efa622c23d939981a96))


## v0.1.1 (2026-09-18)

### Bug Fixes

- Fix gitignore file in template
  ([`612d274`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/612d27404f552bf8dd9f69f7df20f1189a200a1b))

- Fix ruff errors in template
  ([`618281b`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/618281b3114bc01e81ea4a638ba2c50851bbb94f))

- Fix translation setup
  ([`0c58862`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/0c5886251273b2fed6f6e761ea8f01d217aef7d4))

### Features

- Add example unit tests
  ([`c0ac379`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/c0ac3795759678d21ea63f10ca07d79c029581ee))

- Ask for QGIS and python versions to use
  ([`787a054`](https://github.com/osgeosuomi/qgis-plugin-copier-template/commit/787a0543c00b3cb7894824692660241219603aff))


## v0.1.0 (2026-09-03)

- Initial Release
