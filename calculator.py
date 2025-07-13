print("Welcome to the python calculator")
def add(a , b):
    return a + b
def subtract(a , b):
    return a - b
def multiply(a , b):
    return a * b
def division(a , b):
    return a / b
print("Select opertion :")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. division")
while True :
    choice = input("Enter choice from (1/2/3/4): ")
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))
        except ValueError:
            print("Invalid number. please enter a number. ")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=",  subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        next_calculation = input("You want to do next calculation? (y/n):")
        if next_calculation == "n":
            break
        else:
            print("Invalid input")
