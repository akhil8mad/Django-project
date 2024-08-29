def calculate_total(length, breadth=1):
    total = length* breadth
    return total


total_price = calculate_total(10)
print(total_price)    # Example usage with default argument


total_price = calculate_total(5, 3)  # Example usage with overridden default argument
print(total_price)  