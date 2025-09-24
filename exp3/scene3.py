print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def discount_closure(discount_rate):
    # discount_rate should be a value like 0.10 for 10%
    def apply_discount(price):
        discounted_price = price * (1 - discount_rate)
        return round(discounted_price, 2)
    return apply_discount

# Creating multiple discount functions
ten_percent_discount = discount_closure(0.10)
twenty_percent_discount = discount_closure(0.20)
fifty_percent_discount = discount_closure(0.50)

# Applying discounts on different prices
items = [100, 250, 399.99]

print("Original prices:", items)
print("Prices after 10% discount:", [ten_percent_discount(p) for p in items])
print("Prices after 20% discount:", [twenty_percent_discount(p) for p in items])
print("Prices after 50% discount:", [fifty_percent_discount(p) for p in items])
