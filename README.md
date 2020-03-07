# Create public and private keys

```python
import starkbank


private_key = starkbank.key.create(
    path="./user/project/keys"
)
```

# Load existing project
```python
import starkbank


project_user = starkbank.Project(
    id=129837612983,
    private_key=private_key,
    environment=“sandbox”,
)
starkbank.user = project_user
starkbank.debug = True
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


boletos = starkbank.boleto.create([
    starkbank.Boleto(amount=100, due=datetime(2020, 4, 1), ...),
    starkbank.Boleto(amount=200, due=datetime(2020, 4, 1), ...),
])
```

# Get boleto
```python
import starkbank


boleto = starkbank.boleto.get("123")

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


boleto = starkbank.boleto.log.get("123")

print(boleto)
```

# Query boleto-logs
```python
import starkbank
from datetime import datetime

logs = starkbank.boleto.log.query(
    after=datetime(2020, 1, 1),
    before=datetime(2020, 3, 1)
)

for log in logs:
	print(log.id)
```

# Create transfers
```python
import starkbank


transfers = starkbank.transfer.create([
    starkbank.Transfer(amount=100, bank_code="341", ...),
    starkbank.Transfer(amount=200, bank_code="237", ...),
])

print([transfer.id for transfer in transfers])
```

# Get transfer
```python
import starkbank


transfer = starkbank.transfer.get("123")

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
    starkbank.BoletoPayment(barcode="...", tax_id="012.345.678-90", ...),
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
    Transaction(amount=100, receiver_id=200, ...),
    Transaction(amount=200, receiver_id=200, ...),
])

print([transaction.amount for transaction in transactions])
```

# Get transactions
```python
import starkbank


transaction = starkbank.transaction.get("123")

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


webhook = starkbank.webhook.create(url, subscriptions)

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

# Delete webhook events
```python
import starkbank


event = starkbank.webhook.event.delete("123")

print(event.id)
```

# Process webhook events
```python
import starkbank


event = starkbank.webhook.Event(content, signature)

if event.subscription == “transfer”:
    print(event.log.transfer)
    
elif event.subscription == “boleto”:
    print(event.log.boleto)
    
elif event.subscription == “boleto-payment”:
    print(event.log.payment)
```
