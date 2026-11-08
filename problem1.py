def calculatediscount(quantity, price, discountrate):
    subtotal = quantity * price 
    discountamount = subtotal * (discountrate / 100)
    discountedprice = subtotal - discountamount
    return discountamount, discountesprice

quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
discountrate = float(input("Enter discount rate (%): "))

discountamount, discountedprice = calculatediscount(quantity, price, discountrate)

print("Quantity", quantity)
print("Price per item": $, format(price, ".2f"))
print("Discount amount": $, format(discountamount, ".2f"))
print("Discounted price": $, format(discountedprice, ".2f"))
                                  
