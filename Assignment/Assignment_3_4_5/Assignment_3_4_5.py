# Most of the questions in Assignment 3,4 & 5 are theoretical.
# Write a program to accept two numbers and return multiplication.

def main():
    firstNumber = int(input("Enter first number"))
    secondNumber = int(input("Enter second number"))

    result = multiplication(firstNumber, secondNumber)
    print("Multilication is: ", result)

    displayMessage()

def multiplication(firstNumber, secondNumber):
    multiplication = firstNumber * secondNumber
    return multiplication

# Write a program that does not return anything but prints message

def displayMessage():
    print("Completed assignment.")


if __name__ == "__main__":
    main()
    