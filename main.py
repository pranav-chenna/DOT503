def main():
    while True:
        print("Welcome to My Application!")
        print("1. Calculator")
        choice = input("Enter your choice:")

        if choice == "1":
            calculator()

        else:
            print("Invalid choice. Please try again.")


def calculator():
    print("CALCULATOR")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = input("Enter the operation (1-4): ")
    if operation == "1":
        result = num1 + num2
        print("The sum is:", result)
    elif operation == "2":
        result = num1 - num2
        print("The difference is:", result)
    elif operation == "3":
        result = num1 * num2
        print("The product is:", result)
    elif operation == "4":
        result = num1 / num2
        print("The quotient is:", result)
    else:
        print("Invalid operation. Please try again.")

#feature y
def password_generator():
    length = int(input("Enter the length of the password: "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Your password is:", password)
#feature y
if __name__ == '__main__':
    import random

    main()
