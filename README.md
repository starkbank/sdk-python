# Stark Bank Python SDK

Welcome to the Stark Bank Python SDK! This tool is made for Python 
developers who want to easily integrate with our API.
This SDK version is compatible with the Stark Bank API v2.

If you have no idea what Stark Bank is, check out our [website](https://www.starkbank.com/) 
and discover a world where receiving or making payments 
is as easy as sending a text message to your client!

## Supported Python Versions

This library supports the following Python versions:

* Python 2.7
* Python 3.4+

## Stark Bank API documentation

Feel free to take a look at our [API docs](https://www.starkbank.com/docs/api).

## Versioning

This project adheres to the following versioning pattern:

Given a version number MAJOR.MINOR.PATCH, increment:

- MAJOR version when the **API** version is incremented. This may include backwards incompatible changes;
- MINOR version when **breaking changes** are introduced OR **new functionalities** are added in a backwards compatible manner;
- PATCH version when backwards compatible bug **fixes** are implemented.

## Setup

### 1. Install our SDK

1.1 To install the package with pip, run:

```sh
pip install starkbank
```

1.2 To install from source, clone the repo and run:

```sh
python setup.py install
```

### 2. Create your Private and Public Keys

We use ECDSA. That means you need to generate a secp256k1 private
key to sign your requests to our API, and register your public key
with us so we can validate those requests.

You can use one of following methods:

2.1. Check out the options in our [tutorial](https://starkbank.com/faq/how-to-create-ecdsa-keys).

2.2. Use our SDK:

```python
import starkbank

privateKey, publicKey = starkbank.key.create()

# or, to also save .pem files in a specific path
privateKey, publicKey = starkbank.key.create("file/keys/")
```

**NOTE**: When you are creating a new Project, it is recommended that you create the
keys inside the infrastructure that will use it, in order to avoid risky internet
transmissions of your **private-key**. Then you can export the **public-key** alone to the
computer where it will be used in the new Project creation.

### 3. Register your user credentials

You can interact directly with our API using two types of users: Projects and Organizations.

- **Projects** are workspace-specific users, that is, they are bound to the workspaces they are created in.
One workspace can have multiple Projects.
- **Organizations** are general users that control your entire organization.
They can control all your Workspaces and even create new ones. The Organization is bound to your company's tax ID only.
Since this user is unique in your entire organization, only one credential can be linked to it.

3.1 To create a Project in Sandbox:

3.1.1. Log into [Starkbank Sandbox](https://sandbox.web.starkbank.com)

3.1.2. Go to Menu > Projects

3.1.3. Create a Project: Give it a name and upload the public key you created in section 2.

3.1.4. After creating the Project, get its Project ID

3.1.5. Use the Project ID and private key to create the object below:

```python
import starkbank

# Get your private key from an environment variable or an encrypted database.
# This is only an example of a private key content. You should use your own key.
private_key_content = """
-----BEGIN EC PARAMETERS-----
BgUrgQQACg==
-----END EC PARAMETERS-----
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIMCwW74H6egQkTiz87WDvLNm7fK/cA+ctA2vg/bbHx3woAcGBSuBBAAK
oUQDQgAE0iaeEHEgr3oTbCfh8U2L+r7zoaeOX964xaAnND5jATGpD/tHec6Oe9U1
IF16ZoTVt1FzZ8WkYQ3XomRD4HS13A==
-----END EC PRIVATE KEY-----
"""

project = starkbank.Project(
    environment="sandbox",
    id="5656565656565656",
    private_key=private_key_content
)
```

3.2 To register your Organization's public key, a legal representative of your organization must send an e-mail with the desired public key to developers@starkbank.com. This flow will soon be integrated with our website, where you'll be able to do the entire process quicker and independently. Here is an example on how to handle your Organization in the SDK:

```python
import starkbank

# Get your private key from an environment variable or an encrypted database.
# This is only an example of a private key content. You should use your own key.
private_key_content = """
-----BEGIN EC PARAMETERS-----
BgUrgQQACg==
-----END EC PARAMETERS-----
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIMCwW74H6egQkTiz87WDvLNm7fK/cA+ctA2vg/bbHx3woAcGBSuBBAAK
oUQDQgAE0iaeEHEgr3oTbCfh8U2L+r7zoaeOX964xaAnND5jATGpD/tHec6Oe9U1
IF16ZoTVt1FzZ8WkYQ3XomRD4HS13A==
-----END EC PRIVATE KEY-----
"""

organization = starkbank.Organization(
    environment="sandbox",
    id="5656565656565656",
    private_key=private_key_content,
    workspace_id=None,  # You only need to set the workspace_id when you are operating a specific workspace_id
)

# To dynamically use your organization credentials in a specific workspace_id,
# you can use the Organization.replace() function:
starkbank.balance.get(user=starkbank.Organization.replace(organization, "4848484848484848"))
```

NOTE 1: Never hard-code your private key. Get it from an environment variable or an encrypted database.

NOTE 2: We support `'sandbox'` and `'production'` as environments.

NOTE 3: The credentials you registered in `sandbox` do not exist in `production` and vice versa.


### 4. Setting up the user

There are three kinds of users that can access our API: **Organization**, **Project** and **Member**.

- `Project` and `Organization` are designed for integrations and are the ones meant for our SDKs.
- `Member` is the one you use when you log into our webpage with your e-mail.

There are two ways to inform the user to the SDK:

4.1 Passing the user as argument in all functions:

```python
import starkbank

balance = starkbank.balance.get(user=project)  # or organization
```

4.2 Set it as a default user in the SDK:

```python
import starkbank

starkbank.user = project  # or organization

balance = starkbank.balance.get()
```

Just select the way of passing the user that is more convenient to you.
On all following examples we will assume a default user has been set.

### 5. Setting up the error language

The error language can also be set in the same way as the default user:

```python
import starkbank

starkbank.language = "en-US"
```

Language options are "en-US" for english and "pt-BR" for brazilian portuguese. English is default.

## Testing in Sandbox

Your initial balance is zero. For many operations in Stark Bank, you'll need funds
in your account, which can be added to your balance by creating an Invoice or a Boleto. 

In the Sandbox environment, most of the created Invoices and Boletos will be automatically paid,
so there's nothing else you need to do to add funds to your account. Just create
a few Invoices and wait around a bit.

In Production, you (or one of your clients) will need to actually pay this Invoice or Boleto
for the value to be credited to your account.


## Usage

Here are a few examples on how to use the SDK. If you have any doubts, use the built-in
`help()` function to get more info on the desired functionality
(for example: `help(starkbank.boleto.create)`)

### Create transactions

To send money between Stark Bank accounts, you can create transactions:

```python
import starkbank

transactions = starkbank.transaction.create([
    starkbank.Transaction(
        amount=100,  # (R$ 1.00)
        receiver_id="1029378109327810",
        description="Transaction to dear provider",
        external_id="12345",  # so we can block anything you send twice by mistake
        tags=["provider"]
    ),
    starkbank.Transaction(
        amount=234,  # (R$ 2.34)
        receiver_id="2093029347820947",
        description="Transaction to the other provider",
        external_id="12346",  # so we can block anything you send twice by mistake
        tags=["provider"]
    ),
])

for transaction in transactions:
    print(transaction)
```

**Note**: Instead of using Transaction objects, you can also pass each transaction element in dictionary format

### Query transactions

To understand your balance changes (bank statement), you can query
transactions. Note that our system creates transactions for you when
you receive boleto payments, pay a bill or make transfers, for example.

```python
import starkbank

transactions = starkbank.transaction.query(
    after="2020-01-01",
    before="2020-03-01"
)

for transaction in transactions:
    print(transaction)
```

### Get a transaction

You can get a specific transaction by its id:

```python
import starkbank

transaction = starkbank.transaction.get("5155165527080960")

print(transaction)
```

### Get balance

To know how much money you have in your workspace, run:

```python
import starkbank

balance = starkbank.balance.get()

print(balance)
```

### Create transfers

You can also create transfers in the SDK (TED/Pix).

```python
import starkbank
from datetime import datetime, timedelta

transfers = starkbank.transfer.create([
    starkbank.Transfer(
        amount=100,
        bank_code="033",  # TED
        branch_code="0001",
        account_number="10000-0",
        tax_id="012.345.678-90",
        name="Tony Stark",
        tags=["iron", "suit"]
    ),
    starkbank.Transfer(
        amount=200,
        bank_code="20018183",  # Pix
        branch_code="1234",
        account_number="123456-7",
        account_type="salary",
        external_id="my-internal-id-12345",
        tax_id="012.345.678-90",
        name="Jon Snow",
        scheduled=datetime.utcnow() + timedelta(days=3)
    )
])

for transfer in transfers:
    print(transfer)
```

**Note**: Instead of using Transfer objects, you can also pass each transfer element in dictionary format

### Query transfers

You can query multiple transfers according to filters.

```python
import starkbank
from datetime import datetime

transfers = starkbank.transfer.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 4, 1)
)

for transfer in transfers:
    print(transfer.name)
```

### Cancel a scheduled transfer

To cancel a single scheduled transfer by its id, run:

```python
import starkbank

transfer = starkbank.transfer.delete("5155165527080960")

print(transfer)
```

### Get a transfer

To get a single transfer by its id, run:

```python
import starkbank

transfer = starkbank.transfer.get("5155165527080960")

print(transfer)
```

### Get a transfer PDF

A transfer PDF may also be retrieved by its id.
This operation is only valid if the transfer status is "processing" or "success". 

```python
import starkbank

pdf = starkbank.transfer.pdf("5155165527080960")

with open("transfer.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Query transfer logs

You can query transfer logs to better understand transfer life cycles.

```python
import starkbank

logs = starkbank.transfer.log.query(limit=50)

for log in logs:
    print(log.id)
```

### Get a transfer log

You can also get a specific log by its id.

```python
import starkbank

log = starkbank.transfer.log.get("5155165527080960")

print(log)
```

### Create invoices

You can create dynamic QR Code invoices to charge customers or to receive money from accounts
you have in other banks.

```python
# coding: utf-8
import starkbank
from datetime import datetime, timedelta


invoices = starkbank.invoice.create([
    starkbank.Invoice(
        amount=23571,  # R$ 235,71 
        name="Buzz Aldrin",
        tax_id="012.345.678-90", 
        due=datetime(2020, 3, 20),
        expiration=timedelta(hours=3).total_seconds(),
        fine=5,  # 5%
        interest=2.5,  # 2.5% per month
    )
])

for invoice in invoices:
    print(invoice)
```

**Note**: Instead of using Invoice objects, you can also pass each invoice element in dictionary format

### Get an invoice

After its creation, information on an invoice may be retrieved by its id. 
Its status indicates whether it's been paid.

```python
import starkbank

invoice = starkbank.invoice.get("5155165527080960")

print(invoice)
```

### Get an invoice PDF

After its creation, an invoice PDF may be retrieved by its id. 

```python
import starkbank

pdf = starkbank.invoice.pdf("5155165527080960", layout="default")

with open("invoice.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Get an invoice QR Code 

After its creation, an Invoice QR Code may be retrieved by its id. 

```python
import starkbank

qrcode = starkbank.invoice.qrcode("5881614903017472", size= 15)

with open("qrcode.png", "wb") as file:
    file.write(qrcode)
```

Be careful not to accidentally enforce any encoding on the raw png content,
as it may corrupt the file.

### Cancel an invoice

You can also cancel an invoice by its id.
Note that this is not possible if it has been paid already.

```python
import starkbank

invoice = starkbank.invoice.update("5155165527080960", status="canceled")

print(invoice)
```

### Update an invoice

You can update an invoice's amount, due date and expiration by its id.
Note that this is not possible if it has been paid already.

```python
import starkbank
from datetime import datetime, timedelta

invoice = starkbank.invoice.update(
    "5155165527080960",
    amount=100,
    expiration=0,
    due=datetime.utcnow() + timedelta(hours=1),
)

print(invoice)
```

### Query invoices

You can get a list of created invoices given some filters.

```python
import starkbank
from datetime import datetime

invoices = starkbank.invoice.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 3, 1)
)

for invoice in invoices:
    print(invoice)
```

### Query invoice logs

Logs are pretty important to understand the life cycle of an invoice.

```python
import starkbank

logs = starkbank.invoice.log.query(limit=150)

for log in logs:
    print(log)
```

### Get an invoice log

You can get a single log by its id.

```python
import starkbank

log = starkbank.invoice.log.get("5155165527080960")

print(log)
```

### Query deposits

You can get a list of created deposits given some filters.

```python
import starkbank
from datetime import datetime

deposits = starkbank.deposit.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 3, 1)
)

for deposit in deposits:
    print(deposit)
```

### Get a deposit

After its creation, information on a deposit may be retrieved by its id. 

```python
import starkbank

deposit = starkbank.deposit.get("5155165527080960")

print(deposit)
```

### Query deposit logs

Logs are pretty important to understand the life cycle of a deposit.

```python
import starkbank

logs = starkbank.deposit.log.query(limit=150)

for log in logs:
    print(log)
```

### Get a deposit log

You can get a single log by its id.

```python
import starkbank

log = starkbank.deposit.log.get("5155165527080960")

print(log)
```

### Create boletos

You can create boletos to charge customers or to receive money from accounts
you have in other banks.

```python
# coding: utf-8
import starkbank
from datetime import datetime


boletos = starkbank.boleto.create([
    starkbank.Boleto(
        amount=23571,  # R$ 235,71 
        name="Buzz Aldrin",
        tax_id="012.345.678-90", 
        street_line_1="Av. Paulista, 200", 
        street_line_2="10 andar",
        district="Bela Vista", 
        city="São Paulo",
        state_code="SP",
        zip_code="01310-000",
        due=datetime(2020, 3, 20),
        fine=5,  # 5%
        interest=2.5,  # 2.5% per month
    ),
])

for boleto in boletos:
    print(boleto)
```

**Note**: Instead of using Boleto objects, you can also pass each boleto element in dictionary format

### Get a boleto

After its creation, information on a boleto may be retrieved by its id. 
Its status indicates whether it's been paid.

```python
import starkbank

boleto = starkbank.boleto.get("5155165527080960")

print(boleto)
```

### Get a boleto PDF

After its creation, a boleto PDF may be retrieved by its id. 

```python
import starkbank

pdf = starkbank.boleto.pdf("5155165527080960", layout="default")

with open("boleto.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Delete a boleto

You can also cancel a boleto by its id.
Note that this is not possible if it has been processed already.

```python
import starkbank

boleto = starkbank.boleto.delete("5155165527080960")

print(boleto)
```

### Query boletos

You can get a list of created boletos given some filters.

```python
import starkbank
from datetime import datetime

boletos = starkbank.boleto.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 3, 1)
)

for boleto in boletos:
    print(boleto)
```

### Query boleto logs

Logs are pretty important to understand the life cycle of a boleto.

```python
import starkbank

logs = starkbank.boleto.log.query(limit=150)

for log in logs:
    print(log)
```

### Get a boleto log

You can get a single log by its id.

```python
import starkbank

log = starkbank.boleto.log.get("5155165527080960")

print(log)
```

### Investigate a boleto

You can discover if a StarkBank boleto has been recently paid before we receive the response on the next day.
This can be done by creating a BoletoHolmes object, which fetches the updated status of the corresponding
Boleto object according to CIP to check, for example, whether it is still payable or not. The investigation
happens asynchronously and the most common way to retrieve the results is to register a "boleto-holmes" webhook
subscription, although polling is also possible. 

```python
import starkbank

holmes = starkbank.boletoholmes.create([
    starkbank.BoletoHolmes(
        boleto_id="5656565656565656",
    ),
    starkbank.BoletoHolmes(
        boleto_id="4848484848484848",
    ),
])

for sherlock in holmes:
    print(sherlock)
```

**Note**: Instead of using BoletoHolmes objects, you can also pass each payment element in dictionary format

### Get a boleto holmes

To get a single Holmes by its id, run:

```python
import starkbank

sherlock = starkbank.boletoholmes.get("19278361897236187236")

print(sherlock)
```

### Query boleto holmes

You can search for boleto Holmes using filters. 

```python
import starkbank

holmes = starkbank.boletoholmes.query(
    tags=["customer_1", "customer_2"]
)

for sherlock in holmes:
    print(sherlock)
```

### Query boleto holmes logs

Searches are also possible with boleto holmes logs:

```python
import starkbank

logs = starkbank.boletoholmes.log.query(
    holmes_ids=["5155165527080960", "76551659167801921"],
)

for log in logs:
    print(log)
```


### Get a boleto holmes log

You can also get a boleto holmes log by specifying its id.

```python
import starkbank

log = starkbank.boletoholmes.log.get("5155165527080960")

print(log)
```

### Preview a BR Code payment

You can confirm the information on the BR Code payment before creating it with this preview method:

```python
import starkbank

previews = starkbank.brcodepreview.query(brcodes=["00020126580014br.gov.bcb.pix0136a629532e-7693-4846-852d-1bbff817b5a8520400005303986540510.005802BR5908T'Challa6009Sao Paulo62090505123456304B14A"])

for preview in previews:
    print(preview)
```

### Pay a BR Code

Paying a BR Code is also simple. After extracting the BRCode encoded in the Pix QR Code, you can do the following:

```python
import starkbank

payments = starkbank.brcodepayment.create([
    starkbank.BrcodePayment(
        brcode="00020126580014br.gov.bcb.pix0136a629532e-7693-4846-852d-1bbff817b5a8520400005303986540510.005802BR5908T'Challa6009Sao Paulo62090505123456304B14A",
        tax_id="012.345.678-90",
        scheduled="2020-03-13",
        description="this will be fast",
        tags=["pix", "qrcode"],
    )
])

for payment in payments:
    print(payment)
```

**Note**: Instead of using BrcodePayment objects, you can also pass each payment element in dictionary format

### Get a BR Code payment

To get a single BR Code payment by its id, run:

```python
import starkbank

payment = starkbank.brcodepayment.get("19278361897236187236")

print(payment)
```

### Get a BR Code payment PDF

After its creation, a BR Code payment PDF may be retrieved by its id. 

```python
import starkbank

pdf = starkbank.brcodepayment.pdf("5155165527080960")

with open("brcode-payment.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Cancel a BR Code payment

You can cancel a BR Code payment by changing its status to "canceled".
Note that this is not possible if it has been processed already.

```python
import starkbank
from datetime import datetime, timedelta

payment = starkbank.brcodepayment.update(
    "5155165527080960",
    status="canceled"
)

print(payment)
```

### Query BR Code payments

You can search for brcode payments using filters. 

```python
import starkbank

payments = starkbank.brcodepayment.query(
    tags=["company_1", "company_2"]
)

for payment in payments:
    print(payment)
```

### Query BR Code payment logs

Searches are also possible with BR Code payment logs:

```python
import starkbank

logs = starkbank.brcodepayment.log.query(
    payment_ids=["5155165527080960", "76551659167801921"],
)

for log in logs:
    print(log)
```


### Get a BR Code payment log

You can also get a BR Code payment log by specifying its id.

```python
import starkbank

log = starkbank.brcodepayment.log.get("5155165527080960")

print(log)
```


### Pay a boleto

Paying a boleto is also simple.

```python
import starkbank

payments = starkbank.boletopayment.create([
    starkbank.BoletoPayment(
        line="34191.09008 61207.727308 71444.640008 5 81310001234321",
        tax_id="012.345.678-90",
        scheduled="2020-03-13",
        description="take my money",
        tags=["take", "my", "money"],
    ),
    starkbank.BoletoPayment(
        bar_code="34197819200000000011090063609567307144464000",
        tax_id="012.345.678-90",
        scheduled="2020-03-14",
        description="take my money one more time",
        tags=["again"],
    ),
])

for payment in payments:
    print(payment)
```

**Note**: Instead of using BoletoPayment objects, you can also pass each payment element in dictionary format

### Get a boleto payment

To get a single boleto payment by its id, run:

```python
import starkbank

payment = starkbank.boletopayment.get("19278361897236187236")

print(payment)
```

### Get a boleto payment PDF

After its creation, a boleto payment PDF may be retrieved by its id. 

```python
import starkbank

pdf = starkbank.boletopayment.pdf("5155165527080960")

with open("boleto-payment.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Delete a boleto payment

You can also cancel a boleto payment by its id.
Note that this is not possible if it has been processed already.

```python
import starkbank

payment = starkbank.boletopayment.delete("5155165527080960")

print(payment)
```

### Query boleto payments

You can search for boleto payments using filters. 

```python
import starkbank

payments = starkbank.boletopayment.query(
    tags=["company_1", "company_2"]
)

for payment in payments:
    print(payment)
```

### Query boleto payment logs

Searches are also possible with boleto payment logs:

```python
import starkbank

logs = starkbank.boletopayment.log.query(
    payment_ids=["5155165527080960", "76551659167801921"],
)

for log in logs:
    print(log)
```

### Get a boleto payment log

You can also get a boleto payment log by specifying its id.

```python
import starkbank

log = starkbank.boletopayment.log.get("5155165527080960")

print(log)
```

### Create utility payments

Its also simple to pay utility bills (such as electricity and water bills) in the SDK.

```python
import starkbank

payments = starkbank.utilitypayment.create([
    starkbank.UtilityPayment(
        line="34197819200000000011090063609567307144464000",
        scheduled="2020-03-13",
        description="take my money",
        tags=["take", "my", "money"],
    ),
    starkbank.UtilityPayment(
        bar_code="34191.09008 61207.727308 71444.640008 5 81310001234321",
        scheduled="2020-03-14",
        description="take my money one more time",
        tags=["again"],
    ),
])

for payment in payments:
    print(payment)
```

**Note**: Instead of using UtilityPayment objects, you can also pass each payment element in dictionary format

### Query utility payments

To search for utility payments using filters, run:

```python
import starkbank

payments = starkbank.utilitypayment.query(
    tags=["electricity", "gas"]
)

for payment in payments:
    print(payment)
```

### Get a utility payment

You can get a specific bill by its id:

```python
import starkbank

payment = starkbank.utilitypayment.get("5155165527080960")

print(payment)
```

### Get a utility payment PDF

After its creation, a utility payment PDF may also be retrieved by its id. 

```python
import starkbank

pdf = starkbank.utilitypayment.pdf("5155165527080960")

with open("electricity-payment.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Delete a utility payment

You can also cancel a utility payment by its id.
Note that this is not possible if it has been processed already.

```python
import starkbank

payment = starkbank.utilitypayment.delete("5155165527080960")

print(payment)
```

### Query utility payment logs

You can search for payments by specifying filters. Use this to understand the
bills life cycles.

```python
import starkbank

logs = starkbank.utilitypayment.log.query(
    payment_ids=["102893710982379182", "92837912873981273"],
)

for log in logs:
    print(log)
```

### Get a utility payment log

If you want to get a specific payment log by its id, just run:

```python
import starkbank

log = starkbank.utilitypayment.log.get("1902837198237992")

print(log)
```

### Create payment requests to be approved by authorized people in a cost center 

You can also request payments that must pass through a specific cost center approval flow to be executed.
In certain structures, this allows double checks for cash-outs and also gives time to load your account
with the required amount before the payments take place.
The approvals can be granted at our website and must be performed according to the rules
specified in the cost center.

**Note**: The value of the center\_id parameter can be consulted by logging into our website and going
to the desired cost center page.

```python
# coding: utf-8
import starkbank
from datetime import date, timedelta


requests = starkbank.paymentrequest.create([
    starkbank.PaymentRequest(
        center_id="5967314465849344",
        payment=starkbank.Transfer(
            amount=200,
            bank_code="341",
            branch_code="1234",
            account_number="123456-7",
            tax_id="012.345.678-90",
            name="Bucket Head",
            tags=[]
        ),
        due="2020-11-01"
    ),
])

for request in requests:
    print(request)
```

**Note**: Instead of using PaymentRequest objects, you can also pass each request element in dictionary format


### Query payment requests

To search for payment requests, run:

```python
import starkbank

requests = starkbank.paymentrequest.query(center_id=center_id, limit=10)

for request in requests:
    print(request)
```

### Create a webhook subscription

To create a webhook subscription and be notified whenever an event occurs, run:

```python
import starkbank

webhook = starkbank.webhook.create(
    url="https://webhook.site/dd784f26-1d6a-4ca6-81cb-fda0267761ec",
    subscriptions=["transfer", "boleto", "boleto-payment", "boleto-holmes", "brcode-payment", "utility-payment", "deposit", "invoice"],
)

print(webhook)
```

### Query webhooks

To search for registered webhooks, run:

```python
import starkbank

webhooks = starkbank.webhook.query()

for webhook in webhooks:
    print(webhook)
```

### Get a webhook

You can get a specific webhook by its id.

```python
import starkbank

webhook = starkbank.webhook.get("10827361982368179")

print(webhook)
```

### Delete a webhook

You can also delete a specific webhook by its id.

```python
import starkbank

webhook = starkbank.webhook.delete("10827361982368179")

print(webhook)
```

### Process webhook events

It's easy to process events that arrived in your webhook. Remember to pass the
signature header so the SDK can make sure it's really StarkBank that sent you
the event.

```python
import starkbank

response = listen()  # this is the method you made to get the events posted to your webhook endpoint

event = starkbank.event.parse(
    content=response.data.decode("utf-8"),
    signature=response.headers["Digital-Signature"],
)

if event.subscription == "transfer":
    print(event.log.transfer)
    
elif event.subscription == "boleto":
    print(event.log.boleto)
    
elif event.subscription == "boleto-payment":
    print(event.log.payment)

elif event.subscription == "boleto-holmes":
    print(event.log.holmes)

elif event.subscription == "brcode-payment":
    print(event.log.payment)

elif event.subscription == "utility-payment":
    print(event.log.payment)

elif event.subscription == "deposit":
    print(event.log.deposit)

elif event.subscription == "invoice":
    print(event.log.invoice)
```

### Query webhook events

To search for webhooks events, run:

```python
import starkbank

events = starkbank.event.query(after="2020-03-20", is_delivered=False)

for event in events:
    print(event)
```

### Get webhook event

You can get a specific webhook event by its id.

```python
import starkbank

event = starkbank.event.get("10827361982368179")

print(event)
```

### Delete a webhook event

You can also delete a specific webhook event by its id.

```python
import starkbank

event = starkbank.event.delete("10827361982368179")

print(event)
```

### Set webhook events as delivered

This can be used in case you've lost events.
With this function, you can manually set events retrieved from the API as
"delivered" to help future event queries with `is_delivered=False`.

```python
import starkbank

event = starkbank.event.update(id="129837198237192", is_delivered=True)

print(event)
```

### Get DICT key

You can get the Pix key's parameters by its id.

```python
import starkbank

dict_key = starkbank.dictkey.get("tony@starkbank.com")

print(dict_key)
```

### Query your DICT keys

To take a look at the Pix keys linked to your workspace, just run the following:

```python
import starkbank

dict_keys = starkbank.dictkey.query(status="registered")

for dict_key in dict_keys:
    print(dict_key)
```

### Create a Workspace

The Organization user allows you to create new Workspaces (bank accounts) under your organization.
Workspaces have independent balances, statements, operations and users.
The only link between your Workspaces is the Organization that controls them.

**Note**: This route will only work if the Organization user is used with `workspace_id=None`.

```python
import starkbank

workspace = starkbank.workspace.create(
    username="iron-bank-workspace-1",
    name="Iron Bank Workspace 1",
    user=organization,
)

print(workspace)
```

### List your Workspaces

This route lists Workspaces. If no parameter is passed, all the workspaces the user has access to will be listed, but
you can also find other Workspaces by searching for their usernames or IDs directly.

```python
import starkbank

workspaces = starkbank.workspace.query(limit=30)

for workspace in workspaces:
    print(workspace)
```

### Get a Workspace

You can get a specific Workspace by its id.

```python
import starkbank

workspace = starkbank.workspace.get("10827361982368179")

print(workspace)
```

## Handling errors

The SDK may raise one of four types of errors: __InputErrors__, __InternalServerError__, __UnknownError__, __InvalidSignatureError__

__InputErrors__ will be raised whenever the API detects an error in your request (status code 400).
If you catch such an error, you can get its elements to verify each of the
individual errors that were detected in your request by the API.
For example:

```python
import starkbank

try:
    transactions = starkbank.transaction.create([
        starkbank.Transaction(
            amount=99999999999999,  # (R$ 999,999,999,999.99)
            receiver_id="1029378109327810",
            description=".",
            external_id="12345",  # so we can block anything you send twice by mistake
            tags=["provider"]
        ),
    ])
except starkbank.error.InputErrors as exception:
    for error in exception.errors:
        print(error.code)
        print(error.message)
```

__InternalServerError__ will be raised if the API runs into an internal error.
If you ever stumble upon this one, rest assured that the development team
is already rushing in to fix the mistake and get you back up to speed.

__UnknownError__ will be raised if a request encounters an error that is
neither __InputErrors__ nor an __InternalServerError__, such as connectivity problems.

__InvalidSignatureError__ will be raised specifically by starkbank.event.parse()
when the provided content and signature do not check out with the Stark Bank public
key.
