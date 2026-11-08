total = 0
tax_rate = 0.07

def calculate_tax():
    global total

    tax = total * tax_rate
    total_with_tax = total + tax

    return tax, total_with_tax


total = float(input("Enter the total amount: $"))

tax, total_with_tax = calculate_tax()

print(f"Tax: ${tax:.2f}")
print(f"Total with tax: ${total_with_tax:.2f}")
