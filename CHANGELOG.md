# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to the following versioning pattern:

Given a version number MAJOR.MINOR.PATCH, increment:

- MAJOR version when the **API** version is incremented. This may include backwards incompatible changes;
- MINOR version when **breaking changes** are introduced OR **new functionalities** are added in a backwards compatible manner;
- PATCH version when backwards compatible bug **fixes** are implemented.


## [Unreleased]

## [2.5.0] - 2021-02-01
### Added
- Invoice.Payment sub-resource to allow retrieval of invoice payment information

## [2.4.0] - 2021-01-21
### Added
- Transfer.account_type property to allow "checking", "salary" or "savings" account specification
- Transfer.external_id property to allow users to take control over duplication filters

## [2.3.0] - 2021-01-14
### Added
- Organization user
- Workspace resource

## [2.2.2] - 2020-11-24
### Added
- Deposit.account_type parameter
- BrcodePayment.name parameter
### Fixed
- Restrictive requests lib requirements

## [2.2.1] - 2020-11-23
### Fixed
- Added missing pdf parameter from Invoice resource

## [2.2.0] - 2020-11-16
### Added
- Invoice resource to load your account with dynamic QR Codes
- DictKey resource to get DICT (PIX) key parameters
- Deposit resource to receive transfers passively
- PIX support in Transfer resource
- BrcodePayment support to pay static and dynamic PIX QR Codes

## [2.1.0] - 2020-10-27
### Added
- BoletoHolmes to investigate boleto status according to CIP

## [2.0.0] - 2020-10-15
### Added
- PaymentRequest resource to pass payments through manual approval flow

## [0.6.0] - 2020-09-29
### Added
- ids parameter to transaction.query 
- ids parameter to transfer.query
- hidden_fields parameter to Boleto.pdf
- our_number attribute to Boleto
### Fixed
- Boleto.due convertion to datetime.datetime instead of misleading datetime.date

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

