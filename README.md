# Stark Bank Python SDK

The Stark Bank Python SDK serves as an easy integration tool for applications written in Python.
This version of the SDK is compatible with the Stark Bank API v2.

## Stark Bank API documentation

If you want to take a look at our API, follow [this link](https://docs.api.starkbank.com/?version=latest)

## Installation

To install the package with pip, run:

```sh
pip install --upgrade starkbank
```

To install from source, run:

```sh
python setup.py install
```

## Usage

To use the SDK, you need to create a project, which is a special type of user made specially for direct API integrations.
To create your first project, follow [this link](https://www.starkbank.com/project).

Once you have your project, load it in the SDK:

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
    environment="sandbox",  # or production, once you are done testing
)
```

You should pass this project in the user argument of your requests, such as:

```python
balance = starkbank.balance.get(user=project)
```

Alternatively, if you want to use the same project on all requests, we recommend you set it as the default user by doing:

```python
starkbank.user = project

balance = starkbank.balance.get()
```

### Get balance
```python
balance = starkbank.balance.get()

print(balance.amount)
# or simply:
print(balance)
```

# Create boletos
```python
import starkbank
from datetime import datetime


boletos = starkbank.boleto.create([
    starkbank.Boleto(
        amount=10000,  # R$ 100,00 
        name="Buzz Aldrin", 
        tax_id="012.345.678-90", 
        street_line_1="Av. Paulista, 200", 
        street_line_2="10 andar", 
        district="Bela Vista", 
        city="São Paulo", 
        state_code="SP", 
        zip_code="01310-000",
        descriptions=[
            {
                "amount": 0,
                "text": "não aceitar após o vencimento",
            },
            {
                "amount": 100,
                "text": "impostos",
            }
        ]
    ),
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
        fine=10,
        interest=5,
    ),
])
```

# Get boleto
```python
boleto = starkbank.boleto.get("5155165527080960")

print(boleto)
```

# Query boletos
```python
boletos = starkbank.boleto.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 3, 1)
)

for boleto in boletos:
	print(boleto)
```

# Get boleto-log
```python
boleto = starkbank.boleto.log.get("5155165527080960")

print(boleto)
```

# Query boleto-logs
```python
logs = starkbank.boleto.log.query(limit=150)

for log in logs:
	print(log.id)
```

# Create transfers
```python
transfers = starkbank.transfer.create([
    starkbank.Transfer(amount=100, bank_code="200", ...),
    starkbank.Transfer(amount=200, bank_code="200", ...),
])

print([transfer.id for transfer in transfers])
```

# Get transfer
```python
transfer = starkbank.transfer.get("5155165527080960")

print(transfer)
```

# Query transfers
```python
transfers = starkbank.transfer.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 4, 1)
)

for transfer in transfers:
	print(transfer.name)
```

# Create boleto-payments
```python
payments = starkbank.payment.boleto.create([
    starkbank.BoletoPayment(line="...", tax_id="012.345.678-90", ...),
    starkbank.BoletoPayment(bar_code="...", tax_id="012.345.678-90", ...),
])

for payment in payments:
    print(payment)
```

# Get boleto-payment
```python
payment = starkbank.payment.boleto.get("123")

print(payment)
```

# Query boleto-payments
```python
payments = starkbank.payment.boleto.query(
    tags=["company_1", "company_2"]
)

for payment in payments:
	print(payment.id)
```


# Get boleto-payment-log
```python
log = starkbank.payment.boleto.log.get("123")

print(log)
```

# Query boleto-payment-logs
```python
logs = starkbank.payment.boleto.log.query(
    payment_ids=["123", "456"],
)

for log in logs:
	print(log.type)
```

# Create transactions
```python
transactions = starkbank.transaction.create([
    starkbank.Transaction(amount=100, receiver_id="1029378109327810", ...),
    starkbank.Transaction(amount=200, receiver_id="2093029347820947", ...),
])

print([transaction.amount for transaction in transactions])
```

# Get transactions
```python
transaction = starkbank.transaction.get("5155165527080960")

print(transaction)
```

# Query transactions
```python
transactions = starkbank.transaction.query(
    after="2020-01-01",
    before="2020-03-01"
)

for transaction in transactions:
	print(transaction)
```

# Create webhook subscription
```python
webhook = starkbank.webhook.create(
    starkbank.Webhook(
        url="https://webhook.site/dd784f26-1d6a-4ca6-81cb-fda0267761ec",
        subscriptions=["transfer", "charge"],
    )
)

print(webhook.id)

```

# Query webhook
```python
webhooks = starkbank.webhook.query()

for webhook in webhooks:
	print(webhook.id)
```

# Query webhook events
```python
events = starkbank.webhook.event.query(
	is_delivered=False
)

for event in events:
	print(event.id)
```

# Process webhook events
```python
content, signature = listen()

event = starkbank.webhook.Event(content, signature)

if event.subscription == "transfer":
    print(event.log.transfer)
    
elif event.subscription == "boleto":
    print(event.log.boleto)
    
elif event.subscription == "boleto-payment":
    print(event.log.payment)
```

# Handler errors
```python
try:
    transactions = transaction.create([
        Transaction(amount=9999999999, receiver_id="1028937190837", ...),
    ])
except InputErrors as input_errors:
    error_elements = input_errors.elements
    for element in error_elements:
        print(element.code)
        print(element.message)
```

# Generate key pair
```python

private_key, public_key = starkbank.keys.generate("file/keys/")
```


[API docs]: (https://docs.api.starkbank.com/?version=latest)