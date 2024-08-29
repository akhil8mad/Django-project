def calculate_total(a, b, c=0):
    total = a * b
    c = total * c
    final_total = total - c
    return final_total

# Example usage with keyword arguments


final_price = calculate_total(b=3, a=8)
print(final_price)