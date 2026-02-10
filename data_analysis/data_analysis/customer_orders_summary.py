import csv

total_amount = 0
valid_orders = 0

with open("data_entry/cleaned_data/customer_orders_cleaned.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = float(row["amount"])
        if amount > 0:
            total_amount += amount
            valid_orders += 1

print("Total valid sales amount:", total_amount)
print("Number of valid orders:", valid_orders)
