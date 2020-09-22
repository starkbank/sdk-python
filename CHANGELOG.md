# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to the following versioning pattern:

Given a version number MAJOR.MINOR.PATCH, increment:

- MAJOR version when the **API** version is incremented. This may include backwards incompatible changes;
- MINOR version when **breaking changes** are introduced OR **new functionalities** are added in a backwards compatible manner;
- PATCH version when backwards compatible bug **fixes** are implemented.


## [Unreleased]
### Added
- ids parameter to transaction.query 
- ids parameter to transfer.query

### Fixed
- hidden_fields parameter case type

## [0.5.0] - 2020-08-11
### Added
- transfer.scheduled parameter to allow Transfer scheduling
- starkbank.transfer.delete to cancel scheduled Transfers
- Transaction query by tags
### Fixed
- Event errors on unknown subscriptions

## [0.4.0] - 2020-06-03
### Added
- Travis CI setup
- Boleto PDF layout options
- Transfer query tax_id filter
- Global error language option
### Changed
- Test-user credentials to environment variable instead of hard-code
### Fixed
- Python 3.4 bugs
- Docstrings

## [0.3.0] - 2020-05-12
### Added
- "receiver_name" & "receiver_tax_id" property to Boleto entities

## [0.2.1] - 2020-05-05
### Fixed
- Docstrings

## [0.2.0] - 2020-05-04
### Added
- "balance" property to Transaction entities
- Support for dictionaries in create methods
- "discounts" property to Boleto entities
### Fixed
- Docstrings

## [0.1.0] - 2020-04-18
### Added
- Full Stark Bank API v2 compatibility

