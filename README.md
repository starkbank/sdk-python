# Load existing project
```python
import starkbank


project_user = starkbank.Project(
    id=129837612983,
    private_key="""
        -----BEGIN EC PRIVATE KEY-----
        MHQCAQEEIOJ3xkQ9NRdMPLLSrXOOlaoexG8JZgQyTMdX1dISCXaCoAcGBSuBBAAK
        oUQDQgAEUneBQJsBhZl8/nPQd4YUe/UqEAtyJRH01YyWrg+nsNcSRlc1GzC3DB+X
        CPZXBUbsMQAbLoWXIN1pqIX2b/NE9Q==
        -----END EC PRIVATE KEY-----
    """,
    environment="sandbox",
)
starkbank.user = project_user
```

# Get balance
```python
import starkbank


balance = starkbank.balance.get()

print(balance.amount)
```

# Create boletos
```python
import starkbank
from datetime import datetime


boletos = starkbank.boleto.create([
    starkbank.Boleto(amount=100, due=datetime(2020, 4, 1), ...),
    starkbank.Boleto(amount=200, due=datetime(2020, 4, 1), ...),
])
```

# Get boleto
```python
import starkbank


boleto = starkbank.boleto.get("5155165527080960")

print(boleto)
```

# Query boletos
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

# Get boleto-log
```python
import starkbank


boleto = starkbank.boleto.log.get("5155165527080960")

print(boleto)
```

# Query boleto-logs
```python
import starkbank
from datetime import datetime

logs = starkbank.boleto.log.query(limit=150)

for log in logs:
	print(log.id)
```

# Create transfers
```python
import starkbank


transfers = starkbank.transfer.create([
    starkbank.Transfer(amount=100, bank_code="200", ...),
    starkbank.Transfer(amount=200, bank_code="200", ...),
])

print([transfer.id for transfer in transfers])
```

# Get transfer
```python
import starkbank


transfer = starkbank.transfer.get("5155165527080960")

print(transfer)
```

# Query transfers
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

# Create boleto-payments
```python
import starkbank


payments = starkbank.payment.boleto.create([
    starkbank.BoletoPayment(line="...", tax_id="012.345.678-90", ...),
    starkbank.BoletoPayment(bar_code="...", tax_id="012.345.678-90", ...),
])
```

# Get boleto-payment
```python
import starkbank


payment = starkbank.payment.boleto.get("123")

print(payment)
```

# Query boleto-payments
```python
import starkbank
from datetime import datetime

payments = starkbank.payment.boleto.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 3, 1)
)

for payment in payments:
	print(payment.id)
```


# Get boleto-payment-log
```python
import starkbank


log = starkbank.payment.boleto.log.get("123")

print(log)
```

# Query boleto-payment-logs
```python
import starkbank
from datetime import datetime

logs = starkbank.payment.boleto.log.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 3, 1)
)

for log in logs:
	print(log.id)
```

# Create transactions
```python
import starkbank


Transaction = starkbank.Transaction

transactions = starkbank.transaction.create([
    Transaction(amount=100, receiver_id="1029378109327810", ...),
    Transaction(amount=200, receiver_id="2093029347820947", ...),
])

print([transaction.amount for transaction in transactions])
```

# Get transactions
```python
import starkbank


transaction = starkbank.transaction.get("5155165527080960")

print(transaction)
```

# Query transactions
```python
import starkbank


transactions = starkbank.transaction.query(
    after="2020-01-01",
    before="2020-03-01"
)

for transaction in transactions:
	print(transaction)
```

# Create webhook subscription
```python
import starkbank


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
import starkbank


webhooks = starkbank.webhook.query()

for webhook in webhooks:
	print(webhook.id)
```

# Query webhook events
```python
import starkbank


events = starkbank.webhook.event.query(
	is_delivered=False
)

for event in events:
	print(event.id)
```

# Process webhook events
```python
import starkbank
from mylib import listen

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
from starkbank.exception import InputErrors
from starkbank import Transaction, transaction

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
import starkbank


private_key, public_key = starkbank.keys.generate("file/keys/")
```