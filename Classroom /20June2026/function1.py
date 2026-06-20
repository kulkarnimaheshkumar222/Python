def main():
    firstNumber = int(input("Enter first number"))
    secondNumber = int(input("Enter second number"))

    result = addition(firstNumber, secondNumber)

    print("Addition is: ", result)


def addition(firstNumber, secondNumber):

    addition = firstNumber + secondNumber

    return addition


if __name__ == "__main__":
    main()
