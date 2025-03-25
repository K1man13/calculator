def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    Returns both the final price and the discount amount.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price, discount_amount
    else:
        return price, 0

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price and discount amount
final_price, discount_amount = calculate_discount(price, discount_percent)

# Print only the discount amount
print(f"Discount Amount: ${discount_amount:.2f}")
