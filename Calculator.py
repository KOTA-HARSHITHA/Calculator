def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Simple Calculator")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter operation (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = 0

if choice == '1':
    result = add(num1, num2)
    operator = '+'
elif choice == '2':
    result = subtract(num1, num2)
    operator = '-'
elif choice == '3':
    result = multiply(num1, num2)
    operator = '*'
elif choice == '4':
    result = divide(num1, num2)
    operator = '/'
else:
    print("Invalid input")

if type(result) == float:
    print(f"{num1} {operator} {num2} = {result:.2f}")
else:
    print(result)
