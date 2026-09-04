import math


name = "Alex Sharkey"


age = 18


height = 6.175


favorite_color = "green"


circle_area = math.pi * 5 ** 2


print(name)
print(age)
print(height)
print(favorite_color)

print(name, height, favorite_color, age)


# Basic f-string (no format specifier)
print(f"Hello, my name is {name}!")

# Integer format specifier {:d}
print(f"I am {age:d} years old.")

# Float format specifier {:f} - defaults to 6 decimal places
print(f"My height is {height:f} feet.")

# Float with limited decimal places {:.2f}
print(f"My height is {height:.2f} feet.")

# Width and alignment - pad to 10 characters, right-aligned
print(f"Name: {name:>20}")

# Width and alignment - left-aligned
print(f"Name: {name:<20}|")

# Combining variables with specifiers
print(f"{name} is {age:d} years old, {height:.1f} ft tall, and loves {favorite_color}!")


print(f"""
Name: {name}
Age: {age}
Height: {height}
favorite_color: {favorite_color}
""")


print(f"The area of the circle is: {circle_area:.1f}")


print(f"the square root of age is:{math.sqrt(age):.1f}")


print(math.sin(height))
print(math.cos(height))


print(f"the sum of age and 5 is :{age + 5:.1f}")


print(f"the difference between height and 4 is :{height - 4:.1f}")


print(f"the product of age and height is :{age * height:.1f}")


print(f"The quotient of height and 2: {height / 2:.1f}")


print(f"the remainder of age divided by 2 is :{age % 2:.1f}")


print(f"the solution of age raised to the power of 2 is :{age ** 2:.1f}")

Fahrenheit = float (input("Enter a temperature in Fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5 / 9


print(f"{Fahrenheit}°F is {Celsius:.2f}°C")
