# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to the following versioning pattern:

Given a version number MAJOR.MINOR.PATCH, increment:

- MAJOR version when the **API** version is incremented. This may include backwards incompatible changes;
- MINOR version when **breaking changes** are introduced OR **new functionalities** are added in a backwards compatible manner;
- PATCH version when backwards compatible bug **fixes** are implemented.


## [Unreleased]

## [2.29.0] - 2025-07-08
### Added
- InvoicePullRequest resource for requesting payments from subscriptions
- InvoicePullRequest.Log sub-resource
- InvoicePullSubscription resource for creating recurring payment subscriptions  
- InvoicePullSubscription.Log sub-resource
- Support for Automatic Pix feature including manual and automatic payment collection

## [2.28.1] - 2025-04-02
### Added
- support for filtering by 'card_ids' and 'types' in 'query' and 'page' functions for 'MerchantCardLog'
- support for filtering by 'purchase_ids' in 'query' and 'page' functions for 'MerchantInstallment'
- support for filtering by 'installment_ids' and 'types' in 'query' and 'page' functions for 'MerchantInstallmentLog'
- support for filtering by 'purchase_ids' and 'types' in 'query' and 'page' functions for 'MerchantPurchaseLog'
- support for filtering by 'session_ids' and 'types' in 'query' and 'page' functions for 'MerchantSessionLog'

### Removed
- filters for 'status', 'tags' and 'ids' from 'query' and 'page' functions in 'MerchantCardLog', 'MerchantInstallment', 'MerchantInstallmentLog', 'MerchantPurchaseLog' and 'MerchantSessionLog'

## [2.28.0] - 2025-03-02
### Added
- rule parameter on DynamicBrcode resource
- display_description parameter on DynamicBrcode resource

## [2.27.0] - 2025-02-27
### Added
- MerchantSession and MerchantSessionPurchase resources

## [2.26.1] - 2025-02-18
### Fixed
- pytest tests

## [2.26.0] - 2024-07-01
### Added
- request methods
### Changed
- core version
### Fixed
- request prefix param

## [2.25.1] - 2024-04-01
### Fixed
- setup.py install

## [2.25.0] - 2024-03-13
### Added
- SplitProfile resource
- update starkCore version

## [2.24.0] - 2024-02-22
### Added
- function to deposit.log resource get Deposit reversal receipt
- TaxPayment and DarfPayment as PaymentRequest options
### Fixed 
- README import on setup file

## [2.23.0] - 2024-01-22
### Added
- Split resource 
- SplitLog resource
- SplitReceiver resource
- SplitReceiverLog resource
- update function to Deposit resource

## [2.22.0] - 2023-09-18
### Removed 
- account_created, created, owned attributes to DictKey resource
- account_number, branch_code attributes to PaymentPreview resource
### Changed
- account_number, branch_code attributes to DictKey resource
### Fixed 
- account_type docstring attribute to DictKey resource 

## [2.21.0] - 2023-08-06
### Changed
- Transfer account_type parameter to required 

## [2.20.0] - 2023-05-03
### Added
- purpose attribute to CorporateRule resource
- rules attribute to Invoice resource
- Invoice.Rule sub-resource
- description attribute to CorporatePurchase.Log resource

## [2.19.1] - 2023-04-13
### Fixed
- starkcore version import  

## [2.19.0] - 2023-04-11
### Added
- CorporateBalance resource
- CorporateCard resource
- CorporateHolder resource
- CorporateInvoice resource
- CorporatePurchase resource
- CorporateRule resource
- CorporateTransaction resource
- CorporateWithdrawal resource
- CardMethod sub-resource
- MerchantCategory sub-resource
- MerchantCountry sub-resource

## [2.18.1] - 2023-03-23
### Fixed
- import error in Transfer resource

## [2.18.0] - 2023-03-22
### Added
- metadata attribute to Transfer resource
- updated and type attribute to UtilityPayment resource
- workspace_id attribute to Boleto resource
- updated attribute to BoletoHolmes.Log resource
- description attribute to PaymentRequest resource
- picture_url attribute to DynamicBrcode resource
- status, organization_id, picture_url and created attributes to Workspace resource
### Removed
- deprecated BrcodePayment resource 

## [2.17.0] - 2023-01-16
### Added
- DynamicBrcode resource

## [2.16.0] - 2023-01-04
### Added
- picture and pictureType parameters to Workspace.update method
- rules attribute to Transfer resource
- Transfer.Rule sub-resource
- rules attribute to BrcodePayment resource
- BrcodePayment.Rule sub-resource
### Fixed
- nested resource casting
- starkbank.error import
- starkbank.key import
### Changed
- Use starkcore as a dependency.

## [2.15.0] - 2021-11-29
### Added
- query string parameters to POST methods in rest utils [internal]
### Changed
- starkbank-ecdsa library version to 2.0.3

## [2.14.1] - 2021-11-12
### Added
- 'transaction_ids' property to UtilityPayment resource

## [2.14.0] - 2021-11-12
### Added
- 'transaction_ids' property to BoletoPayment, DarfPayment and TaxPayment resources

## [2.13.2] - 2021-11-10
### Changed
- starkbank-ecdsa library version to 2.0.2

## [2.13.1] - 2021-11-04
### Changed
- starkbank-ecdsa library version to 2.0.1

## [2.13.0] - 2021-08-13
### Added
- Support for scheduled invoices, which will display discounts, fine, interest, etc. on the users banking interface when dates are used instead of datetimes

## [2.12.0] - 2021-07-30
### Added
- PaymentPreview resource to preview multiple types of payments before confirmation: BrcodePreview, BoletoPreview, UtilityPreview and TaxPreview

## [2.11.0] - 2021-07-12
### Added
- "payment" account type for Pix related resources
- Institution resource to allow query of institutions recognized by the Brazilian Central Bank for Pix and TED transactions

## [2.10.1] - 2021-06-07
### Fixed
- TaxPayment.scheduled being cast to datetime instead of date

## [2.10.0] - 2021-06-01
### Added
- Normalized event signature verification after failed raw content attempt
- DictKey.bank_name parameter
- Workspace.allowed_tax_ids to control who can send Deposits to the Workspace
- Workspace.update() to allow parameter updates
- TaxPayment resource to allow payment of taxes with bar codes
- DarfPayment resource to allow DARF tax payment without bar code

## [2.9.0] - 2021-03-22
### Added
- Event.Attempt sub-resource to allow retrieval of information on failed webhook event delivery attempts
- Boleto.transaction_ids property to allow transaction tracking
- Transfer.description property to allow control over corresponding Transaction descriptions

## [2.8.0] - 2021-03-09
### Added
- Invoice.link property to allow easy access to invoice webpage
- Event.workspace_id property to allow multiple Workspace Webhook identification
- StarkBankError as base SDK Exception to facilitate general try-excepts
### Fixed
- Bad "+" char URL encoding on BrcodePreview

## [2.7.0] - 2021-02-26
### Added
- pdf function for retrieving PDF receipts from reversed invoice logs 

## [2.6.1] - 2021-02-05
### Fixed
- missing Invoice.transaction_ids property

## [2.6.0] - 2021-02-03
### Added
- page functions as a manual-pagination alternative to queries 

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
