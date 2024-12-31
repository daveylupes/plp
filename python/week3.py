def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

price = float(input("Enter the original price of the item in ZAR (South African Rand): "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print(f"No discount applied. The original price is: R{price:.2f}")
else:
    print(f"The final price after a {discount_percent}% discount is: R{final_price:.2f}")
