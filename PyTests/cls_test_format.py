class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __format__(self, format_spec):
        if format_spec == "s":
            return f"{self.name} ({self.age})"
        elif format_spec == "r":
            return f"{self.name[::-1]} ({self.age})"
        else:
            raise ValueError(f"Invalid format specifier: {format_spec}")

person = Person("Alice", 25)
print("My friend: {:s}".format(person))  # Output: My friend: Alice (25)
print("Reversed name: {:r}".format(person))  # Output: Reversed name: ecilA (25)
print("{:x}".format(person))  # Raises ValueError: Invalid format specifier: x