# Variables and Data Types
x = 5  # Integer
y = 3.14  # Float
name = "AI Developer"  # String
is_student = True  # Boolean
numbers = [1, 2, 3, 4, 5]  # List
person = {"name": "Alex", "age": 25}  # Dictionary

print("Variables:")
print(f"x: {x}, type: {type(x)}")
print(f"y: {y}, type: {type(y)}")
print(f"name: {name}, type: {type(name)}")
print(f"is_student: {is_student}, type: {type(is_student)}")
print(f"numbers: {numbers}, type: {type(numbers)}")
print(f"person: {person}, type: {type(person)}")

# Control Structures: Conditionals
print("\nConditionals:")
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Control Structures: Loops
print("\nLoops:")
for num in numbers:
    print(f"Number: {num}")

# Basic List Operations
print("\nList Operations:")
numbers.append(6)  # Add to list
print(f"Updated numbers: {numbers}")
print(f"Sum of numbers: {sum(numbers)}")

# Functions
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print("\nFunction Example:")
avg = calculate_average(numbers)
print(f"Average of numbers: {avg}")