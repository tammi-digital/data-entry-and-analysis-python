records = [
    {"name": "Anna", "email": "anna@gmail.com", "amount": 120},
    {"name": "Bob", "email": "", "amount": -50},
    {"name": "Chris", "email": "chris@yahoo.com", "amount": 75}
]

for r in records:
    if r["email"] == "":
        print("Missing email:", r["name"])
    elif r["amount"] <= 0:
        print("Invalid amount:", r["name"])
    else:
        print("Valid record:", r["name"])
