# Welcome Message
from art import logo
print(logo)

intro = input("Power on Calculator : Enter 'yes' or 'no' ").lower()
while True:
    if intro == "yes":
        pass
    elif intro == "no":
        break
    else:
        print("This is a wrong input")
        print('Try Again!!! 🙁🙁🙁')
        break
    print("👉🏼 Welcome to TifeLabs Calculator😁😁😁")
    def addition(first_digit, second_digit):
        result = first_digit + second_digit
        return result

    def subtraction(first_digit, second_digit):
        result = first_digit - second_digit
        return result

    def multiplication(first_digit, second_digit):
        result = first_digit * second_digit
        return result

    def division(first_digit, second_digit):
        if second_digit == 0:
            return "Cannot divide by zero"
        result = first_digit / second_digit
        return result

    user1 = int(input("ENTER FIRST DIGIT >> "))
    user2 = int(input("ENTER SECOND DIGIT >> "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter choice (1/2/3/4): "))

    if choice == 1:
        result = addition(user1, user2)
        print("Result:", result)
    elif choice == 2:
        result = subtraction(user1, user2)
        print("Result:", result)
    elif choice == 3:
        result = multiplication(user1, user2)
        print("Result:", result)
    elif choice == 4:
        result = division(user1, user2)
        print("Result:", result)
    else:
        print("Invalid input")

