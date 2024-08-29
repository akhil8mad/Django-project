def greet(name, message="hello"):
    print(f"Hello, {name}! {message}")

# Example usage with keyword arguments
# greet(name="Akhil", message="How are you?")
# greet(message="Nice to see you!", name="Akhil")

greet("Akhil","hi")
greet("Akhil",message="hi")

greet(name="akhil","hi")  # right side cannot be default

greet("hello","akhil")