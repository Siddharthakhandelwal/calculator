def add_numbers(x,y):
    return x + y

def subtract(x,y):
    return x - y

def Divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

x= int(input("Enter first number: "))
y= int(input("Enter second number: "))

print("what do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice=int(input("Enter choice (1/2/3/4): "))

if choice == 1:
    print("Result:", add_numbers(x,y))
elif choice == 2:
    print("Result:", subtract(x,y))
elif choice == 3:
    print("Result:")
elif choice == 4:
    print("Result:" divide(x,y))

