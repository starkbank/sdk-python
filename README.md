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
* Python 3.5+

## Stark Bank API documentation

If you want to take a look at our API, follow [this link](https://docs.api.starkbank.com/?version=latest).

## Installation

To install the package with pip, run:

```sh
pip install starkbank
```

To install from source, clone the repo and run:

```sh
python setup.py install
```

## Creating a Project

To connect to the Stark Bank API, you need user credentials. We currently have 2
kinds of users: Members and Projects. Given the purpose of this SDK, it only
supports Projects, which is a type of user made specially for direct API
integrations. To start using the SDK, create your first Sandbox Project in our 
[website](https://sandbox.web.starkbank.com) in the Project session.

Once you've created your project, load it in the SDK:

```python
import starkbank

project = starkbank.Project(
    id=129817512982,
    private_key="""
        -----BEGIN EC PRIVATE KEY-----
        MHQCAQEEIOJ3xkQ9NRdMPLLSrX3OlaoexG8JZgQyTMdX1eISCXaCoBcGBSuBBAAK
        oUQDQgAEUneBQJsBhZl8/nPQd4YUe/UqEAtyJRH01YyWrg+nsNcSRlc1GzC3DB+X
        CPZXBUbsMQAbLoWXIN1pqIX2b/NE9Q==
        -----END EC PRIVATE KEY-----
    """,
    environment="sandbox",
)
```

Once you are done testing and want to move to Production, create a new Project
in your Production account ([click here](https://web.starkbank.com)). Also,
when you are loading your Project, change the environment from `"sandbox"` to
`"production"` in the constructor shown above. 

NOTE: Never hard-code your private key. Get it from an environment variable, for example. 

## Setting up the user

You can inform the project to the SDK in two different ways.

The first way is passing the user argument in all methods, such as:

```python
import starkbank

balance = starkbank.balance.get(user=project)
```

Or, alternatively, if you want to use the same project on all requests,
we recommend you set it as the default user by doing:

```python
import starkbank

starkbank.user = project

balance = starkbank.balance.get()
```

Just select the way of passing the project user that is more convenient to you.
On all following examples we will assume a default user has been set.

## Testing in Sandbox

Your initial balance is zero. For many operations in Stark Bank, you'll need funds
in your account, which can be added to your balance by creating a Boleto. 

In the Sandbox environment, 90% of the created Boletos will be automatically paid,
so there's nothing else you need to do to add funds to your account. Just create
a few and wait around a bit.

In Production, you (or one of your clients) will need to actually pay this Boleto
for the value to be credited to your account.


## Usage

Here are a few examples on how to use the SDK. If you have any doubts, use the built-in
`help()` function to get more info on the desired functionality
(for example: `help(starkbank.boleto.create)`)

### Get balance

To know how much money you have in your workspace, run:

```python
import starkbank

balance = starkbank.balance.get()

print(balance)
```

### Create boletos

You can create boletos to charge customers or to receive money from accounts
you have in other banks.

```python
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

### Get boleto

After its creation, information on a boleto may be retrieved by passing its id. 
Its status indicates whether it's been paid.

```python
import starkbank

boleto = starkbank.boleto.get("5155165527080960")

print(boleto)
```

### Get boleto PDF

After its creation, a boleto PDF may be retrieved by passing its id. 

```python
import starkbank

pdf = starkbank.boleto.pdf("5155165527080960")

with open("boleto.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Delete boleto

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

### Create transfers

You can also create transfers in the SDK (TED/DOC).

```python
import starkbank

transfers = starkbank.transfer.create([
    starkbank.Transfer(
        amount=100,
        bank_code="200",
        branch_code="0001",
        account_number="10000-0",
        tax_id="012.345.678-90",
        name="Tony Stark",
        tags=["iron", "suit"]
    ),
    starkbank.Transfer(
        amount=200,
        bank_code="341",
        branch_code="1234",
        account_number="123456-7",
        tax_id="012.345.678-90",
        name="Jon Snow",
        tags=[]
    )
])

for transfer in transfers:
    print(transfer)
```

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

### Get transfer

To get a single transfer by its id, run:

```python
import starkbank

transfer = starkbank.transfer.get("5155165527080960")

print(transfer)
```

### Get transfer PDF

After its creation, a transfer PDF may also be retrieved by passing its id. 

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

### Pay a boleto

Paying a boleto is also simple.

```python
import starkbank

payments = starkbank.payment.boleto.create([
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

### Get boleto payment

To get a single boleto payment by its id, run:

```python
import starkbank

payment = starkbank.payment.boleto.get("19278361897236187236")

print(payment)
```

### Get boleto payment PDF

After its creation, a boleto payment PDF may be retrieved by passing its id. 

```python
import starkbank

pdf = starkbank.payment.boleto.pdf("5155165527080960")

with open("boleto_payment.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Delete boleto payment

You can also cancel a boleto payment by its id.
Note that this is not possible if it has been processed already.

```python
import starkbank

payment = starkbank.payment.boleto.delete("5155165527080960")

print(payment)
```

### Query boleto payments

You can search for boleto payments using filters. 

```python
import starkbank

payments = starkbank.payment.boleto.query(
    tags=["company_1", "company_2"]
)

for payment in payments:
    print(payment)
```

### Query boleto payment logs

Searches are also possible with boleto payment logs:

```python
import starkbank

logs = starkbank.payment.boleto.log.query(
    payment_ids=["5155165527080960", "76551659167801921"],
)

for log in logs:
    print(log)
```


### Get boleto payment log

You can also get a boleto payment log by specifying its id.

```python
import starkbank

log = starkbank.payment.boleto.log.get("5155165527080960")

print(log)
```

### Create utility payment

Its also simple to pay utility bills (such electricity and water bills) in the SDK.

```python
import starkbank

payments = starkbank.payment.utility.create([
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

### Query utility payments

To search for utility payments using filters, run:

```python
import starkbank

payments = starkbank.payment.utility.query(
    tags=["electricity", "gas"]
)

for payment in payments:
    print(payment)
```

### Get utility payment

You can get a specific bill by its id:

```python
import starkbank

payment = starkbank.payment.utility.get("5155165527080960")

print(payment)
```

### Get utility payment PDF

After its creation, a utility payment PDF may also be retrieved by passing its id. 

```python
import starkbank

pdf = starkbank.payment.utility.pdf("5155165527080960")

with open("electricity_payment.pdf", "wb") as file:
    file.write(pdf)
```

Be careful not to accidentally enforce any encoding on the raw pdf content,
as it may yield abnormal results in the final file, such as missing images
and strange characters.

### Delete utility payment

You can also cancel a utility payment by its id.
Note that this is not possible if it has been processed already.

```python
import starkbank

payment = starkbank.payment.utility.delete("5155165527080960")

print(payment)
```

### Query utility bill payment logs

You can search for payments by specifying filters. Use this to understand the
bills life cycles.

```python
import starkbank

logs = starkbank.payment.utility.log.query(
    payment_ids=["102893710982379182", "92837912873981273"],
)

for log in logs:
    print(log)
```

### Get utility bill payment log

If you want to get a specific payment log by its id, just run:

```python
import starkbank

log = starkbank.payment.utility.log.get("1902837198237992")

print(log)
```

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

### Get transaction

You can get a specific transaction by its id:

```python
import starkbank

transaction = starkbank.transaction.get("5155165527080960")

print(transaction)
```

### Create webhook subscription

To create a webhook subscription and be notified whenever an event occurs, run:

```python
import starkbank

webhook = starkbank.webhook.create(
    url="https://webhook.site/dd784f26-1d6a-4ca6-81cb-fda0267761ec",
    subscriptions=["transfer", "boleto", "boleto-payment", "utility-payment"],
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

### Get webhook

You can get a specific webhook by its id.

```python
import starkbank

webhook = starkbank.webhook.get("10827361982368179")

print(webhook)
```

### Delete webhook

You can also delete a specific webhook by its id.

```python
import starkbank

webhook = starkbank.webhook.delete("10827361982368179")

print(webhook)
```

### Process webhook events

Its easy to process events that arrived in your webhook. Remember to pass the
signature header so the SDK can make sure its really StarkBank that sent you
the event.

```python
import starkbank

response = listen()  # this is the method you made to get the events posted to your webhook

event = starkbank.webhook.event.parse(content=response.content, signature=response.headers["Digital-Signature"])

if event.subscription == "transfer":
    print(event.log.transfer)
    
elif event.subscription == "boleto":
    print(event.log.boleto)
    
elif event.subscription == "boleto-payment":
    print(event.log.payment)
```

### Query webhook events

To search for webhooks events, run:

```python
import starkbank

events = starkbank.webhook.event.query(after="2020-03-20", is_delivered=False)

for event in events:
    print(events)
```

### Get webhook event

You can get a specific webhook event by its id.

```python
import starkbank

event = starkbank.webhook.event.get("10827361982368179")

print(event)
```

### Delete webhook event

You can also delete a specific webhook event by its id.

```python
import starkbank

event = starkbank.webhook.event.delete("10827361982368179")

print(event)
```

### Set webhook events as delivered

This can be used in case you've lost events.
With this function, you can manually set events retrieved from the API as
"delivered" to help future event queries with `is_delivered=False`.

```python
import starkbank

events = starkbank.webhook.event.set_delivered(id="129837198237192")

for event in events:
    print(event)
```

## Handling errors

The SDK may raise one of four types of errors: __InputErrors__, __InternalServerError__, __UnknownException__, __InvalidSignatureException__

__InputErrors__ will be raised whenever the API detects an error in your request (status code 400).
If you catch such an error, you can get its elements to verify each of the
individual errors that were detected in your request by the API.
For example:

```python
import starkbank

try:
    transactions = starkbank.transaction.create([
        starkbank.Transaction(
            amount=99999999999999,  # (R$ 1.00)
            receiver_id="1029378109327810",
            description=".",
            external_id="12345",  # so we can block anything you send twice by mistake
            tags=["provider"]
        ),
    ])
except starkbank.exception.InputErrors as exception:
    for error in exception.errors:
        print(error.code)
        print(error.message)
```

__InternalServerError__ will be raised if the API runs into an internal error.
If you ever stumble upon this one, rest assured that the development team
is already rushing in to fix the mistake and get you back up to speed.

__UnknownException__ will be raised if a request encounters an error that is
neither __InputErrors__ nor an __InternalServerError__, such as connectivity problems.

__InvalidSignatureException__ will be raised specifically by starkbank.webhook.event.parse()
when the provided content and signature do not check out with the Stark Bank public
key.

## Key pair generation

The SDK provides a helper to allow you to easily create ECDSA secp256k1 keys to use
within our API. If you ever need a new pair of keys, just run:

```python
import starkbank

private_key, public_key = starkbank.key.create()

# or, to also save .pem files in a specific path
private_key, public_key = starkbank.key.create("file/keys/")
```

NOTE: When you are creating a new Project, it is recommended that you create the
keys inside the infrastructure that will use it, in order to avoid risky internet
transmissions of your **private-key**. Then you can export the **public-key** alone to the
computer where it will be used in the new Project creation.


[API docs]: (https://docs.api.StarkBank.com/?version=v2)