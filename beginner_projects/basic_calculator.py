def add(a, b):
    print(f'Your solution: {a} + {b} = {a + b}')


def sub(a, b):
    print(f'Your solution: {a} - {b} = {a - b}')


def mult(a, b):
    print(f'Your solution: {a} * {b} = {a * b}')


def div(a, b):
    print(f'Your solution: {a} / {b} = {a / b}')


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("Input your choice: ").lower()
    if choice == "a":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "b":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a, b)
    elif choice == "c":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        mult(a, b)
    elif choice == "d":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        div(a, b)
    elif choice == "e":
        print("program ended")
        quit()
    else:
        print("Invalid choice! ")
        quit()
