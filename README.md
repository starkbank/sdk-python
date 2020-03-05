# Load existing project
```python
import starkbank

project_user = starkbank.project.Project(
    id=129837612983,
    private_key=“...PEM...“,
)
```

# Create new project
```python
import starkbank

member_user = starkbank.member.Member(
    email=“my@email.com”,
    workspace_id=198273912783,
    private_key=“...PEM...“,
)

# or

member_user = starkbank.member.Member(
    email=“my@email.com”,
    workspace_id=198273912783,
    password=“minha senha muito longa”,
)

project_user = starkbank.project.create(
    user=member_user,
    name=“Meu projeto em python”,
    allowedIps=[],
    public_key=None,  # gera aleatoriamente
)

```

# Create new session
```python
...
import starkbank

session_user = starkbank.session.create(
    user=project_user,
    public_key=None,  # gera aleatoriamente
)
```

# Get balance

```python
...
import starkbank

balance = starkbank.balance.get(user=session_user)
print(balance.amount)
```

# Create transactions

```python
...
import starkbank

Transaction = starkbank.transaction.Transaction
transactions = [
    Transaction(amount=100, bank_code=200, ...),
    Transaction(amount=200, bank_code=200, ...),
]
transactions = starkbank.transaction.create(
    user=session_user,
    transactions=transactions,
)
print([transaction.amount for transaction in transactions])
```

# Process webhook events

```python
...
import starkbank

event = starkbank.webhook.event_from_json(listen())
if event.subscription == “transfer”:
    print(event.amount)
elif event.subscription == “boleto”:
    print(event.scheduled)
```
