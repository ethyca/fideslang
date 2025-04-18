# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/)

The types of changes are:

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Developer Experience` for changes in developer workflow or tooling.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## [Unreleased](https://github.com/ethyca/fideslang/compare/3.1.0...main)


## [3.1.0](https://github.com/ethyca/fideslang/compare/3.0.9...3.1.0)

### Deprecated
- Deprecated `Cookies` model and `.cookies` property on `System` and `PrivacyDeclaration` [#199](https://github.com/ethyca/fideslang/pull/27)


## [3.0.9](https://github.com/ethyca/fideslang/compare/3.0.8...3.0.9)

### Added

- Add field-level masking strategy overrides [#23](https://github.com/ethyca/fideslang/pull/23)

## [3.0.8](https://github.com/ethyca/fideslang/compare/3.0.7...3.0.8)

### Changed

- Remove stipulation that sub fields (Field) of a Field object cannot have data categories assigned [#22](https://github.com/ethyca/fideslang/pull/22)

## [3.0.7](https://github.com/ethyca/fideslang/compare/3.0.6...3.0.7)

### Added

- Add a loosely-typed `partitioning` field to the `DatasetCollection.fides_meta` structure to support flexible database table partitioning specifications [#21](https://github.com/ethyca/fideslang/pull/21)


## [3.0.6](https://github.com/ethyca/fideslang/compare/3.0.5...3.0.6)

### Changed

- Add collection-level masking strategy overrides and support specifying one collection to be erased after another [#17](https://github.com/ethyca/fideslang/pull/17)


## [3.0.5](https://github.com/ethyca/fideslang/compare/3.0.4...3.0.5)

### Added

- Adds namespace field to dataset fides_meta [#18](https://github.com/ethyca/fideslang/pull/18)

## [3.0.4](https://github.com/ethyca/fideslang/compare/3.0.3...3.0.4)

### Added

- Adds mappings and new data use for special purposes 3 [#15](https://github.com/ethyca/fideslang/pull/15)


## [3.0.3](https://github.com/ethyca/fideslang/compare/3.0.2...3.0.3)
- Add custom_request_field to FidesMeta [#13](https://github.com/ethyca/fideslang/pull/13)

## [3.0.2](https://github.com/ethyca/fideslang/compare/3.0.1...3.0.2)

### Changed

- Upgrades Pydantic for V2 support and removes support for Pydantic V1 [#11](https://github.com/ethyca/fideslang/pull/11)
- Removes Python 3.8 from supported versions [#11](https://github.com/ethyca/fideslang/pull/11)

## [3.0.1](https://github.com/ethyca/fideslang/compare/3.0.0...3.0.1)

### Added

- Added a `vendor_deleted_date` field to the `System` model [#10](https://github.com/ethyca/fideslang/pull/10)

## [3.0.0](https://github.com/ethyca/fideslang/compare/2.2.2...3.0.0)

### Removed

- Removed `DataQualifier` construct and all references [#186](https://github.com/ethyca/fideslang/pull/186)
- Removed `Registry` construct and all references [#186](https://github.com/ethyca/fideslang/pull/186)
- Removed deprecated fields on `System`, `DataUse` and `Dataset` models. [#186](https://github.com/ethyca/fideslang/pull/186)


## [2.2.2](https://github.com/ethyca/fideslang/compare/2.2.1...2.2.2)

### Added

- Give Flexible Legal Basis a default of True [#184](https://github.com/ethyca/fideslang/pull/184)


## [2.2.1](https://github.com/ethyca/fideslang/compare/2.2.0...2.2.1)

### Added 

- Added a `System.cookies` property to support `Cookie` records explicitly associated with a `System` generally [#181](https://github.com/ethyca/fideslang/pull/181)
- Added a `System.previous_vendor_id` property to support to associate a `System` record with a "deprecated" vendor record [#182](https://github.com/ethyca/fideslang/pull/182)

## [2.2.0](https://github.com/ethyca/fideslang/compare/2.1.0...2.2.0)

### Added

- Added support for new TCF-based `System` fields [#173](https://github.com/ethyca/fideslang/pull/173)
- Added support for `PrivacyDeclaration.flexible_legal_basis_for_profiling` field [#177](https://github.com/ethyca/fideslang/pull/177) [#178](https://github.com/ethyca/fideslang/pull/178)
- Added GVL data category mapping and functions [#175](https://github.com/ethyca/fideslang/pull/175) [#180](https://github.com/ethyca/fideslang/pull/180)

### Changed

- Changed default taxonomy and GVL mapping to support GVL Purpose 11 [#171](https://github.com/ethyca/fideslang/pull/171) [#174](https://github.com/ethyca/fideslang/pull/174)

### Fixed

- Removed mistaken trailing `.` on some data category `name`s in the default taxonomy [#169](https://github.com/ethyca/fideslang/pull/169)


## [2.1.0](https://github.com/ethyca/fideslang/compare/2.0.4...2.1.0)

### Added 

- Added GVL mappings and utility functions [#167](https://github.com/ethyca/fideslang/pull/167)


## [2.0.4](https://github.com/ethyca/fideslang/compare/2.0.3...2.0.4)


### Changed

- Add Collection > Fides Meta > Skip Processing Flag to skip collections in DSR processing [#165](https://github.com/ethyca/fideslang/pull/165)


## [2.0.3](https://github.com/ethyca/fideslang/compare/2.0.2...2.0.3)

### Changed

- Relax system legal basis for transfer fields [#162](https://github.com/ethyca/fideslang/pull/162)


## [2.0.2](https://github.com/ethyca/fideslang/compare/2.0.1...2.0.2)

### Changed

- Update `system.legal_basis_for_profiling` and `system.legal_basis_for_transfers` fields [#156](https://github.com/ethyca/fideslang/pull/156)

## [2.0.1](https://github.com/ethyca/fideslang/compare/2.0.0...2.0.1)

### Changed

- Fix validation around the new FidesVersion type [#151](https://github.com/ethyca/fideslang/pull/151)

### Fixed

- Fix docs site for fideslang 2.0.0 [#154](https://github.com/ethyca/fideslang/pull/154)

## [2.0.0](https://github.com/ethyca/fideslang/compare/1.4.4...2.0.0)

### Changed

- Updated the Data Categories and Data Uses to support GVL [#144](https://github.com/ethyca/fideslang/pull/144)
- Add version metadata to the default taxonomy items [#147](https://github.com/ethyca/fideslang/pull/147)


## [1.4.6 (Hotfix)](https://github.com/ethyca/fideslang/compare/1.4.5...1.4.6)

### Changed

- Relax system legal basis for transfer fields [#162](https://github.com/ethyca/fideslang/pull/162)


## [1.4.5 (Hotfix)](https://github.com/ethyca/fideslang/compare/1.4.4...1.4.5)

### Changed

- Update `system.legal_basis_for_profiling` and `system.legal_basis_for_transfers` fields [#156](https://github.com/ethyca/fideslang/pull/156)

## [1.4.4](https://github.com/ethyca/fideslang/compare/1.4.3...1.4.4)

### Changed

- Add new fields to System and Privacy Declarations to support GVL [#146](https://github.com/ethyca/fideslang/pull/146)

### Added

- Add versioning metadata as fields on Taxonomy Data types [#147](https://github.com/ethyca/fideslang/pull/147)

### Changed

- Updated the Data Categories and Data Uses to support GVL [#144](https://github.com/ethyca/fideslang/pull/144)

### Fixed

- Don't allow duplicate entries for DatasetCollections as part of Datasets [#136](https://github.com/ethyca/fideslang/pull/136)
- Cython/PyYAML versions breaking builds [#145](https://github.com/ethyca/fideslang/pull/145)

## [1.4.3](https://github.com/ethyca/fideslang/compare/1.4.2...1.4.3)

### Changed

- Consolidate Python build tooling into `pyproject.toml` [#135](https://github.com/ethyca/fideslang/pull/135)

## [1.4.2](https://github.com/ethyca/fideslang/compare/1.4.1...1.4.2)

### Added

- Support Pydantic <1.11 [#122] (https://github.com/ethyca/fideslang/pull/122)

### Changed

- Add `Cookies` schema and similar property to `PrivacyDeclaration` [#115](https://github.com/ethyca/fideslang/pull/115)

### Fixed

- Fix Fideslang visual explorer on docs site [#123](https://github.com/ethyca/fideslang/pull/123)
- Fix Fideslang key finding function [#131](https://github.com/ethyca/fideslang/pull/131)

### Developer Experience

- Allow Docker to select plaform [#121] https://github.com/ethyca/fideslang/pull/121
- Use build time versioneer [#120] https://github.com/ethyca/fideslang/pull/120

## [1.4.1](https://github.com/ethyca/fideslang/compare/1.4.0...1.4.1)

### Changed

- Make `meta` property of `System` and `Dataset` models more permissive [#113](https://github.com/ethyca/fideslang/pull/113)

## [1.4.0](https://github.com/ethyca/fideslang/compare/1.3.4...1.4.0)

### Changed

- Updated the default data uses [#107](https://github.com/ethyca/fideslang/pull/107)

### Removed

- The `system_dependencies` field of `System` resources [#105](https://github.com/ethyca/fideslang/pull/105)

## [1.3.4](https://github.com/ethyca/fideslang/compare/1.3.3...1.3.4)

### Changed

- Make `PrivacyDeclaration` use pydantic `orm_mode` [#101](https://github.com/ethyca/fideslang/pull/101)

## [1.3.3](https://github.com/ethyca/fideslang/compare/1.3.2...1.3.3)

### Changed

- Make `PrivacyDeclation.name` optional [#97](https://github.com/ethyca/fideslang/pull/97)

## [1.3.2](https://github.com/ethyca/fideslang/compare/1.3.1...1.3.2)

### Changed

- Update css to brand colors, edit footer [#87](https://github.com/ethyca/fideslang/pull/87)
- Moved over DSR concepts into Fideslang. Expanded allowable characters for FideKey and added additional Dataset validation. [#95](https://github.com/ethyca/fideslang/pull/95)
- Docs css and link updates [#93](https://github.com/ethyca/fideslang/pull/93)

## [1.3.1](https://github.com/ethyca/fideslang/compare/1.3.0...1.3.1)

### Fixed

- `DataFlow` resource models included in `System` resource models are now exported to valid YAML [#89](https://github.com/ethyca/fideslang/pull/89)

## [1.3.0](https://github.com/ethyca/fideslang/compare/1.2.0...1.3.0)

### Added

- The `DataFlow` resource model defines a resource with which a `System` resource may communicate [#85](https://github.com/ethyca/fideslang/pull/85)
- `PrivacyDeclaration`s may define `egress` and `ingress`, to contextualize communications with other resources [#85](https://github.com/ethyca/fideslang/pull/85)

### Deprecated

- The `dataset_references` field of `PrivacyDeclaration` resources [#85](https://github.com/ethyca/fideslang/pull/85)
- The `system_dependencies` field of `System` resources [#85](https://github.com/ethyca/fideslang/pull/85)

### Developer Experience

- The `DataFlow` resource model is exposed when importing `fideslang` [#85](https://github.com/ethyca/fideslang/pull/85)

### Docs

- Updated the brand colors and footer on the docs site [#87](https://github.com/ethyca/fideslang/pull/87)

### Fixed

- Fixed broken links in docs [#74](https://github.com/ethyca/fideslang/pull/74)
- Pydantic 1.10.0 was causing issues so specified the pydantic version needs to be less than 1.10.0 [#79](https://github.com/ethyca/fideslang/pull/79)
- Resolved a circular import in `default_taxonomy.py` [#85](https://github.com/ethyca/fideslang/pull/85)

## [1.2.0](https://github.com/ethyca/fideslang/compare/1.1.0...1.2.0)

### Added

- New field `is_default` added to DataCategory, DataUse, DataSubject, and DataQualifier [#68](https://github.com/ethyca/fideslang/pull/68)
- Return invalid key values as part of the stack trace for easier debugging [#55](https://github.com/ethyca/fideslang/pull/55)

### Docs

- Updated documentation for new Data Category and Use taxonomy [#69](https://github.com/ethyca/fideslang/pull/69)

### Changed

- Docker images now use Debian `bullseye` instead of `buster`

### Fixed

- Add setuptools to dev-requirements to fix versioneer error [#72](https://github.com/ethyca/fideslang/pull/72)

## 1.1.0

### Changed

- Simplification of Data Categories and Data Uses [#62](https://github.com/ethyca/fideslang/pull/62)

## 1.0.0

### Added

- There is now a `tags` field on the `FidesModel` model [#45](https://github.com/ethyca/fideslang/pull/45)
- Add DatasetFieldBase model [#49](https://github.com/ethyca/fideslang/pull/49)

## 0.9.0

### Added

- Created the fideslang standalone python module

### Developer Experience

- Added a py.typed file
